import time
import random

numero = int(input("Informe um número: "))

sorteio = 0
while sorteio != numero:
    sorteio = random.randint(0, 30)
    print(sorteio)
    time.sleep(1)

print("O numero foi descoberto:", sorteio)
