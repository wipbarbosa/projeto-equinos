from machine import ADC, Pin
import time
from envio import conectar_wifi, enviar

# conectar no wifi
conectar_wifi()

# sensor no pino VP
sensor = ADC(Pin(34))
sensor.atten(ADC.ATTN_11DB)

# pinos
lo_mais = Pin(32, Pin.IN)
lo_menos = Pin(33, Pin.IN)

# valor que conta um batimento
LIMIAR = 30000

# guardar o tempo do ultimo batimento contado
ultimo_batimento = 0
primeiro_batimento = True

# saber se o sinal estava acima do limiar na leitura anterior
estava_acima = False

# guardar o ultimo bpm e quando ele foi enviado
bpm = 0
novo_bpm = False
ultimo_envio = 0

while True:

    # avisar se o eletrodo tiver solto
    if lo_mais.value() == 1 or lo_menos.value() == 1:
        print("Sensor esta solto")
        primeiro_batimento = True # recomeça a contagem quando o eletrodo voltar
        bpm = 0
        time.sleep(0.5)
        continue

    # ler o sensor
    valor = sensor.read_u16()
    acima = valor > LIMIAR

    agora = time.ticks_ms() # pega o tempo atual
    tempo = time.ticks_diff(agora, ultimo_batimento) # quanto tempo desde o ultimo batimento

    # contar so quando o sinal CRUZA o limiar (subida), e se passou 0.3 s do ultimo
    if acima and not estava_acima and tempo > 300:
        if primeiro_batimento:
            # o primeiro so marca o tempo, ainda nao da pra calcular o bpm
            primeiro_batimento = False
        else:
            bpm = 60000 // tempo # dividir minuto pelo tempo entre 2 batimentos
            print("BPM", bpm)
            novo_bpm = True
        ultimo_batimento = agora # guardar batimento como o mais recente

    estava_acima = acima

    # mandar o bpm para a api a cada 2 segundos, so se teve batimento novo
    # (a api so aceita bpm entre 10 e 250)
    if novo_bpm and time.ticks_diff(agora, ultimo_envio) > 2000:
        if 10 <= bpm <= 250:
            enviar(bpm)
        novo_bpm = False
        ultimo_envio = agora

    time.sleep(0.001)
