"""API do Monitoramento Cardíaco Equino (Flask + MySQL).

Rodar:  python app.py      (porta 8000)
Antes:  executar schema.sql no MySQL Workbench.

Configuração do banco por variáveis de ambiente (ou edite os padrões abaixo):
  DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME
"""
import os
from datetime import datetime, timezone

import pymysql
from flask import Flask, jsonify, request
from flask_cors import CORS
from pymysql.cursors import DictCursor

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": int(os.getenv("DB_PORT", "3306")),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", ""),
    "database": os.getenv("DB_NAME", "equino"),
    "charset": "utf8mb4",
    "cursorclass": DictCursor,
    "autocommit": True,
}

OFFLINE_APOS_SEGUNDOS = 10  # sem medição há mais que isso = dispositivo offline
BPM_MIN, BPM_MAX = 10, 250  # fora disso é leitura inválida

app = Flask(__name__)
app.json.ensure_ascii = False
CORS(app)


# ---------- utilitários ----------
def conectar():
    return pymysql.connect(**DB_CONFIG)


def agora_utc():
    # DATETIME do MySQL não guarda fuso: guardamos sempre em UTC
    return datetime.now(timezone.utc).replace(tzinfo=None, microsecond=0)


def iso(dt):
    return dt.isoformat() + "Z" if dt else None


def erro(msg, status):
    return jsonify({"erro": msg}), status


@app.errorhandler(pymysql.MySQLError)
def erro_banco(e):
    app.logger.error("Erro no MySQL: %s", e)
    return erro("Erro ao acessar o banco de dados", 503)


# ---------- cavalos ----------
@app.post("/cavalos")
def criar_cavalo():
    dados = request.get_json(silent=True) or {}
    nome = str(dados.get("nome", "")).strip()
    if not nome or len(nome) > 80:
        return erro("Campo 'nome' obrigatório (até 80 caracteres)", 422)
    with conectar() as con, con.cursor() as cur:
        cur.execute("INSERT INTO cavalos (nome, criado_em) VALUES (%s, %s)", (nome, agora_utc()))
        return jsonify({"id": cur.lastrowid, "nome": nome}), 201


@app.get("/cavalos")
def listar_cavalos():
    with conectar() as con, con.cursor() as cur:
        cur.execute(
            """SELECT c.id, c.nome, GROUP_CONCAT(d.id) AS dispositivos
               FROM cavalos c LEFT JOIN dispositivos d ON d.cavalo_id = c.id
               GROUP BY c.id, c.nome ORDER BY c.id"""
        )
        return jsonify(cur.fetchall())


@app.post("/cavalos/<int:cavalo_id>/dispositivo")
def vincular_dispositivo(cavalo_id):
    """Liga (ou religa) um dispositivo a um cavalo."""
    dados = request.get_json(silent=True) or {}
    device_id = str(dados.get("device_id", "")).strip()
    if not device_id or len(device_id) > 50:
        return erro("Campo 'device_id' obrigatório (até 50 caracteres)", 422)
    with conectar() as con, con.cursor() as cur:
        cur.execute("SELECT 1 FROM cavalos WHERE id = %s", (cavalo_id,))
        if cur.fetchone() is None:
            return erro("Cavalo não encontrado", 404)
        cur.execute(
            """INSERT INTO dispositivos (id, cavalo_id) VALUES (%s, %s)
               ON DUPLICATE KEY UPDATE cavalo_id = VALUES(cavalo_id)""",
            (device_id, cavalo_id),
        )
        return jsonify({"device_id": device_id, "cavalo_id": cavalo_id}), 201


# ---------- medições ----------
@app.post("/medicoes")
def receber_medicao():
    """Endpoint que o ESP32 (ou o simulador) chama. O horário é carimbado aqui."""
    dados = request.get_json(silent=True)
    if not isinstance(dados, dict):
        return erro("Corpo deve ser um JSON", 422)

    device_id = str(dados.get("device_id", "")).strip()
    bpm = dados.get("bpm")
    signal_ok = dados.get("signal_ok", True)

    if not device_id or len(device_id) > 50:
        return erro("Campo 'device_id' obrigatório", 422)
    if isinstance(bpm, bool) or not isinstance(bpm, int) or not (BPM_MIN <= bpm <= BPM_MAX):
        return erro(f"Campo 'bpm' deve ser inteiro entre {BPM_MIN} e {BPM_MAX}", 422)
    if not isinstance(signal_ok, bool):
        return erro("Campo 'signal_ok' deve ser true ou false", 422)

    with conectar() as con, con.cursor() as cur:
        cur.execute("SELECT cavalo_id FROM dispositivos WHERE id = %s", (device_id,))
        disp = cur.fetchone()
        if disp is None or disp["cavalo_id"] is None:
            return erro("Dispositivo não cadastrado ou sem cavalo vinculado", 404)
        cur.execute(
            """INSERT INTO medicoes (cavalo_id, dispositivo_id, bpm, signal_ok, criado_em)
               VALUES (%s, %s, %s, %s, %s)""",
            (disp["cavalo_id"], device_id, bpm, int(signal_ok), agora_utc()),
        )
    return jsonify({"ok": True}), 201


@app.get("/cavalos/<int:cavalo_id>/medicoes")
def historico(cavalo_id):
    """Últimas medições (mais recente primeiro)."""
    limite = request.args.get("limite", default=100, type=int)
    limite = max(1, min(limite, 5000))
    with conectar() as con, con.cursor() as cur:
        cur.execute(
            """SELECT bpm, signal_ok, dispositivo_id, criado_em FROM medicoes
               WHERE cavalo_id = %s ORDER BY criado_em DESC, id DESC LIMIT %s""",
            (cavalo_id, limite),
        )
        linhas = cur.fetchall()
    for r in linhas:
        r["signal_ok"] = bool(r["signal_ok"])
        r["criado_em"] = iso(r["criado_em"])
    return jsonify(linhas)


@app.get("/cavalos/<int:cavalo_id>/resumo")
def resumo(cavalo_id):
    """BPM atual, mín/máx/média da janela pedida e status da conexão."""
    minutos = request.args.get("minutos", default=60, type=int)
    minutos = max(1, min(minutos, 1440))
    with conectar() as con, con.cursor() as cur:
        cur.execute("SELECT id, nome FROM cavalos WHERE id = %s", (cavalo_id,))
        cav = cur.fetchone()
        if cav is None:
            return erro("Cavalo não encontrado", 404)

        cur.execute(
            """SELECT bpm, criado_em FROM medicoes WHERE cavalo_id = %s
               ORDER BY criado_em DESC, id DESC LIMIT 1""",
            (cavalo_id,),
        )
        ultima = cur.fetchone()

        cur.execute(
            """SELECT COUNT(*) AS total, MIN(bpm) AS minimo, MAX(bpm) AS maximo, AVG(bpm) AS media
               FROM medicoes
               WHERE cavalo_id = %s AND signal_ok = 1
                 AND criado_em >= UTC_TIMESTAMP() - INTERVAL %s MINUTE""",
            (cavalo_id, minutos),
        )
        est = cur.fetchone()

    segundos, online = None, False
    if ultima:
        segundos = int((agora_utc() - ultima["criado_em"]).total_seconds())
        online = segundos <= OFFLINE_APOS_SEGUNDOS

    return jsonify(
        {
            "cavalo": cav,
            "bpm_atual": ultima["bpm"] if ultima else None,
            "ultima_medicao": iso(ultima["criado_em"]) if ultima else None,
            "segundos_desde_ultima": segundos,
            "dispositivo_online": online,
            "janela_minutos": minutos,
            "total": est["total"],
            "minimo": est["minimo"],
            "maximo": est["maximo"],
            "media": round(float(est["media"]), 1) if est["media"] is not None else None,
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)