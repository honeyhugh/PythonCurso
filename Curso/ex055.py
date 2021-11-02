pesado = 0
leve = 0
for c in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa em Kg: '.format(c)))
    if c == 1: # melhor forma, pra n colocar "99999" no 'leve'
        leve = peso
        pesado = peso
    if pesado <= peso:
        pesado = peso
    elif peso <= leve:
        leve = peso
print('O maior peso digitado foi {}Kg e o menor foi {}Kg.'.format(pesado, leve))
