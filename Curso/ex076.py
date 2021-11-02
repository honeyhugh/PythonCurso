itens = 'Livro', 59.90, 'Mouse', 45.00, 'Joystick Ípega', 129.90, 'Notebook', 2.500, 'Garrafa de Ursinho', 30.00, \
    'Celular Samsung', 1530
print('_' * 50)
print(f'{"LISTAGEM DE PREÇOS":=^50}')
print('_' * 50)
for pos in range(0, len(itens)):
    if pos % 2 == 0:
        print(f'{itens[pos]:.<40}', end='')
    else:
        print(f'R${itens[pos]:7.2f}')
print('_' * 50)
