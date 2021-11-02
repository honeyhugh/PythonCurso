total = caro = cont = preço = barato = 0
nomebarato = resp = ' '
while True:
    cont += 1
    nome = input('Digite o nome do produto: ').strip()
    preço = float(input('Digite o preço do produto: R$'))
    total += preço
    if cont == 1 or preço < barato:
        barato = preço
        nomebarato = nome
    if preço >= 1000:
        caro += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Continuar? [S/N] ')).strip().upper()[0]
        print('=' * 30)
    if resp in 'N':
            break
print(f'O total gasto foi R${total:.2f}.')
print(f'{caro} produtos custam mais de R$1000,00')
print(f'E o produto mais barato foi {nomebarato} custando R${barato}')
