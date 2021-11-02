times = 'Sport', 'Bradesco Esportes', 'Nosso Clube', 'São José BasketBall',\
        'Aeroclube', 'Joinville', 'Sociedade Thalia'
print(f'Os times do campeonato brasileiro são: {times}')
print('=' * 50)
print(f'Os 5 primeiros colocados são: {times[0:5]}')
print('=' * 50)
print(f'Os quatro últimos colocados são: {times[-4:]}')
print('=' * 50)
print(f'Times em ordem alfabética: {sorted(times)}')
print('=' * 50)
print(f'E o time São José BasketBall está na posição {times.index("São José BasketBall") + 1}ª posição')
print('=' * 50)
