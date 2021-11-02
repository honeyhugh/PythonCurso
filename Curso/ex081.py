n = []
while True:
    n.append(int(input('Digite um valor: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp in 'N':
        break
print(f'No total, foram digitados {len(n)} termos')
n.sort(reverse=True)
print(f'Os termos, em ordem decrescente, são: {n}')
if 5 in n:
    print(f'E o número 5 foi digitado {n.count(5)} vezes')
else:
    print('E o número 5 foi digitado nenhuma vez.')
