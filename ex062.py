print('==Analisador de uma Progressão Aritmética==')
a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
print('Os 10 primeiros termos dessa PA são: ')
cont = 0
termo = a1
n = 1
while cont != 10:
    cont += 1
    if cont == 1:
        print('{}, '.format(a1), end='')
    else:
        termo += r
        print('{}, '.format(termo) if cont != 10 else '{}.'.format(termo), end='')
cont = 0
while n != 0:
    cont = 0
    print('\nQuer continuar vendo mais termos?')
    n = int(input('Digite a nova quantidade (0 para finalizar): '))
    termo = a1
    for c in range(a1, n * r, r):
        cont += 1
        print('{}'.format(c) if cont == n else '{}, '.format(c), end='')
print('Programa finalizado com sucesso.')

# prof fez um melhor, como menos linha, mas o meu ta ok.
