valores = []
valorespar = []
valoresimp = []
while True:
    n = int(input('Digite um valor: '))
    valores.append(n)
    if n % 2 == 0:
        valorespar.append(n)
    else:
        valoresimp.append(n)
    esc = ' '
    while esc not in 'NS':
        esc = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if esc in 'N':
        break
print(f'Os valores digitados foram: {valores}')
print((f'A lista de pares é: {valorespar}'))
print(f'A lista de ímpares é: {valoresimp}')
