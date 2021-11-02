n1 = int(input('Digite um número: '))
n2 = int(input('Digite o segundo: '))
n3 = int(input('Digite o terceiro: '))
resultado = n1
if n2 > n1 and n2 > n3:
    resultado = n2
if n3 > n1 and n3 > n2:
    resultado = n3
r2 = n1
if n2 < n1 and n2 < n3:
    r2 = n2
if n3 < n1 and n3 < n2:
    r2 = n3
print('Entre {}, {} e {} o maior número é o {} e o menor é {}.'.format(n1, n2, n3, resultado, r2))
