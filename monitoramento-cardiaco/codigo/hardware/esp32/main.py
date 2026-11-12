from machine import ADC, Pin
import time

# sensor no pino VP
sensor = ADC(Pin(36))
sensor.atten(ADC.ATTN_11DB)

# pinos
lo_mais = Pin(32, Pin.IN)
lo_menos = Pin(33, Pin.IN)

# valor que conta um batimento
LIMIAR = 50000

# guardar o tempo do ultimo batimento contado
ultimo_batimento = 0

while True:

    # avisar se o eletrodo tiver solto
    if lo_mais.value() == 1 or lo_menos.value() == 1:
        print("Sensor esta solto")
        time.sleep(0.5)
        continue

    # ler o sensor
    valor = sensor.read_u16()
    print(valor)

    agora = time.ticks_ms() # pega o tempo atual
    tempo = time.ticks_diff(agora, ultimo_batimento) # quanto tempo desde o ultimo batimento

    # contar apenas se passar de 0.3 segundos do ultimo
    if valor > LIMIAR and tempo > 300: # dividir minuto pelo tempo de 2 batimentos
        bpm = 60000 // tempo
        print("BPM", bpm)
        ultimo_batimento = agora # guardar batimento como o mais recente

    time.sleep(0.1)