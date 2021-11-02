n1 = int(input('Digite o 1º termo: '))
r = int(input('Digite a razão: '))
print('Os dez primeiros termos dessa PA são:')
for c in range(n1, n1 + 10 * r, r):
    print(c, end=', ')
print('fim')
