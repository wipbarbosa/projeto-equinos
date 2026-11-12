# Monitoramento Cardíaco Equino

```
ESP32 --(Wi-Fi, HTTP/JSON)--> API (Flask) --> MySQL --> Dashboard
```

## 1. Criar o banco

No MySQL Workbench, abra `backend/schema.sql` e execute tudo (raio ⚡).
Isso cria o banco `equino`, as tabelas e o cavalo "Trovão" ligado ao dispositivo `esp32-01`.

## 2. Rodar o backend

```bash
cd backend
pip install -r requirements.txt
```

Informe a senha do seu MySQL (Windows PowerShell):

```powershell
$env:DB_PASSWORD="sua_senha"
python app.py
```

Linux/Mac: `DB_PASSWORD=sua_senha python app.py`.
Se o usuário não for `root`, defina também `DB_USER`. Alternativa: editar os padrões em `DB_CONFIG` no `app.py`.

A API sobe em http://localhost:8000.

## 3. Testar sem ESP32

Em outro terminal:

```bash
python simulador.py
```

Conferir no navegador:
- http://localhost:8000/cavalos/1/resumo
- http://localhost:8000/cavalos/1/medicoes?limite=20

No Workbench: `SELECT * FROM equino.medicoes ORDER BY id DESC;`

## 4. Testar no Wokwi

O ESP32 do Wokwi não acessa o `localhost` do seu PC. Exponha a API com um túnel:

```bash
ngrok http 8000        # ou: cloudflared tunnel --url http://localhost:8000
```

1. Crie um projeto **ESP32 MicroPython** em wokwi.com.
2. Adicione `esp32/envio.py` e substitua o `main.py` pelo da pasta `esp32/`.
3. Em `envio.py`, coloque a URL do túnel em `API_URL` (terminando em `/medicoes`).
4. Rode a simulação e acompanhe o resumo no navegador.

## 5. Quando o kit chegar

No `esp32/main.py`, troque `bpm_simulado(...)` pelo BPM suavizado calculado a partir do AD8232 e mantenha `enviar(bpm)` a cada 1–2 s, fora do laço de amostragem rápida. Ajuste `WIFI_SSID` e `WIFI_SENHA` em `envio.py`.

## Endpoints

| Método | Rota | Função |
|---|---|---|
| POST | `/medicoes` | Recebe `{device_id, bpm, signal_ok}` (horário de Brasília carimbado pelo servidor) |
| GET | `/cavalos` | Lista cavalos |
| POST | `/cavalos` | Cadastra cavalo (`{nome}`) |
| POST | `/cavalos/<id>/dispositivo` | Vincula um dispositivo (`{device_id}`) |
| GET | `/cavalos/<id>/medicoes` | Histórico |
| GET | `/cavalos/<id>/resumo` | BPM atual, mín/máx/média, status de conexão |
