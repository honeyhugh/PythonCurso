n = int(input('Digite um fatorial (sem a exclamação): '))
cont = 0
resultado = 0
while cont != n:
    if cont and resultado == 0:
        resultado = 1
    cont += 1
    resultado = resultado * cont
    if cont == 1:
        print('{} '.format(cont), end='')
    else:
        print('x {}'.format(cont), end=' ')
print('= {}'.format(resultado))

# o do professor ficou levemente melhor, mas ta ok
