pessoas = list()
dado = list()
resp = ' '
print('=====Analisador de Pesos =====')
while True:
    print('=' * 30)
    dado.append(input('Nome: '))
    dado.append(float(input('Peso: ')))
    pessoas.append(dado[:])
    dado.clear()
    resp = ' '
    while resp not in 'NS':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if 'N' in resp:
        break
m = max(pessoas)[1]
n = min(pessoas)[1]
for p in pessoas:
    if m == p[1]:
        print(p[0])
print('=' * 30)
print(f'No total, {len(pessoas)} pessoas foram cadastradas.')
print(f'O maior peso foi de {m}kg. Peso de ', end='')
for p in pessoas:
    if m == p[1]:
        print(p[0], end=' > ')
print(f'\nO menor peso foi de {n}kg. Peso de ', end='')
for p in pessoas:
    if n == p[1]:
        print(p[0], end=' > ')
print()
print('=' * 30)
