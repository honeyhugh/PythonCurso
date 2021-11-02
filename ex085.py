par = []
impar = []
valores = []
for c in range(0, 7):
    n = int(input(f'Digite o {c + 1}º valor: '))
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
valores.append(par)
valores.append(impar)
valores[0].sort()
valores[1].sort()
print(f'Os valores pares são: {valores[0]}')
print(f'Os valores ímpares são: {valores[1]}')


# Resolução do professor (melhor)

valores = [[], []]
n = 0
for c in range(1, 8):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        valores[0].append(n)
    else:
        valores[1].append(n)
valores[0].sort()
valores[1].sort()
print(f'Os números pares digitados foram: {valores[0]}')
print(f'Os valores ímpares digitados foram: {valores[1]}')
