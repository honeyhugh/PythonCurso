from random import randint
from time import sleep
lista = []
jogo = []
n = int(input('Quantos jogos gostaria de fazer? '))
for c in range(0, n):
    while len(jogo) != 6:
        numero = randint(1, 60)
        if numero not in jogo:
            jogo.append(numero)
    lista.append(jogo[:])
    jogo.clear()
lista.sort()
for j in range(0, n):
    print(lista[j])
    sleep(0.5)
