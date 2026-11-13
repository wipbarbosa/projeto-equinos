import esp32
from time import sleep, sleep_ms

import ujson
import urequests
import network
import time

print("Connecting to WiFi", end="")
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
#Arruma conforme o nome da internet e afins, onde ta vazio vai a senha
sta_if.connect('Visitantes', '')
while not sta_if.isconnected():
  print(".", end="")
  time.sleep(0.1)
print(" Connected!")

def mensagem():
    # Define the endpoint URL
    url = "https://6zlxye.api.infobip.com/whatsapp/1/message/template"

    # Define the payload as a standard Python dictionary
    payload = {
        "messages": [
            {
                "from": "447860088970",
                "to": "5541992862805",
                "messageId": "d5b4f9a2-ad8c-4d92-ad82-2b565d3f4bec",
                "content": {
                    "templateName": "test_whatsapp_template_en",
                    "templateData": {
                        "body": {
                            "placeholders": ["Nabo"]
                        }
                    },
                    "language": "en"
                }
            }
        ]
    }

    # Define the headers
    headers = {
        'Authorization': 'App 7e6fb5cb49187432e41a72a2e91071c0-1dde876a-fe08-40ca-9490-e8ff9d75843d',
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    try:
        # Send the POST request using urequests
        response = urequests.post(url, data=ujson.dumps(payload), headers=headers)
    
        # Print the response text
        print("mensagem enviada com sucesso! Sua égua esta em trabalho de parto", response.text)
    
        # Always close the response to free up socket resources
        response.close()

    except Exception as e:
        print("An error occurred:", e)

def distanciaVulva(valor):
    if valor >= 32 :
        mensagem()
    else:
        print("Égua ainda não ta pra parir")

def ler_hall(amostras=50):
    total = 0
    for _ in range(amostras):
        total += esp32.hall_sensor()
        sleep_ms(2)
    return total / amostras

while True:
    distancia = ler_hall()
    print("O valor do sensor é:  ", distancia)
    distanciaVulva(distancia)
    sleep(0.5)
