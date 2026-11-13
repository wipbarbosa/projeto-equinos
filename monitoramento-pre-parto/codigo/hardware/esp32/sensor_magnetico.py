import esp32
from time import sleep, sleep_ms

def ler_hall(amostras=50):
    total = 0
    for _ in range(amostras):
        total += esp32.hall_sensor()
        sleep_ms(2)
    return total / amostras

while True:
    valor = ler_hall()
    print("O valor do sensor é:  ", valor)
    sleep(0.5)
