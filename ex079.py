n = []
esc = ' '
while True:
    valor = int(input('Digite um valor: '))
    if valor not in n:
        n.append(valor)
    else:
        print('Esse valor já existe na lista e por isso foi descartado.')
    esc = ' '
    while esc not in 'SN':
        esc = input('Quer continuar? [S/N] ').upper().strip()
    if esc in 'N':
            break
print(f'Os números digitados foram {sorted(n)}')
