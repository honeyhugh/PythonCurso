s = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        cont = cont + 1
        s = s + n
print('Você digitou {} números pares, e a soma deles é {}'.format(cont, s))
