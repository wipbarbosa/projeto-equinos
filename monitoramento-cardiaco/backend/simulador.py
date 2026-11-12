"""Simula o ESP32 enviando BPM para a API (só biblioteca padrão, sem pip).

Uso:  python simulador.py
      python simulador.py http://localhost:8000 esp32-01
Ciclo de 80 s: repouso -> exercício -> recuperação.
"""
import json
import random
import sys
import time
import urllib.request

API = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8000"
DEVICE_ID = sys.argv[2] if len(sys.argv) > 2 else "esp32-01"
INTERVALO_S = 2


def bpm_simulado(t):
    t = t % 80
    if t < 20:        # repouso
        base = 35
    elif t < 50:      # exercício: sobe de 35 até 180
        base = 35 + (t - 20) / 30 * 145
    else:             # recuperação: desce de 180 até 40
        base = 180 - (t - 50) / 30 * 140
    return int(base + random.uniform(-2, 2))


def enviar(bpm):
    corpo = json.dumps({"device_id": DEVICE_ID, "bpm": bpm, "signal_ok": True}).encode()
    req = urllib.request.Request(
        f"{API}/medicoes", data=corpo, headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=5) as r:
        return r.status


inicio = time.time()
while True:
    bpm = bpm_simulado(time.time() - inicio)
    try:
        print(f"BPM {bpm} -> HTTP {enviar(bpm)}")
    except Exception as e:
        print("Falha no envio:", e)
    time.sleep(INTERVALO_S)
