from math import fabs
print('==Tabuada==')
while True:
    n = int(input('Digite um valor: '))
    if n != fabs(n):
        break
    cont = 1
    while cont != 11:
        print(f'{n} x {cont:2} = {cont * n}')
        cont += 1
print('Programa finalizado com sucesso.')