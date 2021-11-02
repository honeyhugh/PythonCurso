n = list()
for c in range(0, 5):
    n.append(int(input(f'Digite um número na posição {c}: ')))
print(f'Os números digitados foram: {n[0]}, {n[1]}, {n[2]}, {n[3]} e {n[4]}')
print(f'O maior valor foi {max(n)} nas posições ', end='')
for pos, val in enumerate(n):
    if max(n) == val:
        print(f'{pos}...', end=' ')
print(f'\nE o menor valor foi {min(n)} nas posições ', end='')
for pos, val in enumerate(n):
    if min(n) == val:
        print(f'{pos}...', end=' ')
