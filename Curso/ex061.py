print('==Analisador de uma Progressão Aritmética==')
a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
print('Os 10 primeiros termos dessa PA são: ')
cont = 0
termo = a1
while cont != 10:
    cont += 1
    if cont == 1:
        print('{}, '.format(a1), end='')
    else:
        termo += r
        print('{}, '.format(termo) if cont != 10 else '{}.'.format(termo), end='')
