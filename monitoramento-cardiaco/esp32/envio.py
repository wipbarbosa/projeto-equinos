"""Wi-Fi + envio do BPM para a API. Serve no Wokwi e no ESP32 real."""
import json
import network
import time

try:
    import urequests as requests
except ImportError:
    import requests

# --- configuração ---
WIFI_SSID = "Wokwi-GUEST"   # no ESP32 real: nome da sua rede
WIFI_SENHA = ""             # no ESP32 real: senha da rede
API_URL = "https://SEU-TUNEL.ngrok-free.app/medicoes"  # troque pela URL do túnel
DEVICE_ID = "esp32-01"


def conectar_wifi(timeout_s=20):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if wlan.isconnected():
        return True
    print("Conectando ao Wi-Fi...")
    wlan.connect(WIFI_SSID, WIFI_SENHA)
    t0 = time.time()
    while not wlan.isconnected():
        if time.time() - t0 > timeout_s:
            print("Wi-Fi: tempo esgotado")
            return False
        time.sleep(0.5)
    print("Wi-Fi conectado:", wlan.ifconfig()[0])
    return True


def wifi_ok():
    return network.WLAN(network.STA_IF).isconnected()


def enviar(bpm, signal_ok=True):
    """Envia uma medição. Retorna True se a API aceitou."""
    corpo = json.dumps({"device_id": DEVICE_ID, "bpm": bpm, "signal_ok": signal_ok})
    headers = {
        "Content-Type": "application/json",
        "ngrok-skip-browser-warning": "1",  # inofensivo se não usar ngrok
    }
    try:
        r = requests.post(API_URL, data=corpo, headers=headers)
        ok = 200 <= r.status_code < 300
        if not ok:
            print("API respondeu", r.status_code)
        r.close()
        return ok
    except Exception as e:
        print("Falha no envio:", e)
        return False
