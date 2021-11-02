from time import sleep
from math import fabs


def contador(a, b, c):
    cont = list()
    cont.append(a)
    if c == 0:
        c = 1
    if c < 0:
        c = int(fabs(c))
    if a < b:
        while cont[-1] < b:  # c Positivo
            item = cont[-1] + c
            if item <= b:
                cont.append(item)
            else:
                break
    if b < a:
        while cont[-1] > b:  # c Negativo
            item = cont[-1] - c
            if item >= b:
                cont.append(item)
            else:
                break
    print(f'Contagem de {a} até {b} de {c} em {c} passos:')
    for i in cont:
        print(i, end=' ', flush=True)
        sleep(0.5)
    print()


contador(1, 10, 1)
print('-=' * 20)
contador(10, 0, 1)
print('-=' * 20)
print('Gostaria de tentar?')
while True:
    resp = ' '
    inicio = int(input('Digite o início: '))
    fim = int(input('Digige o final: '))
    passo = int(input('De quantos em quantos passos? '))
    contador(inicio, fim, passo)
    while resp not in 'SN':
        resp = str(input('Gostaria de tentar de novo? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
