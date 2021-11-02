def area(a, b):
    area = a * b
    print(f'O terreno de {a}mx{b}m mede {area}m².')


# Programa Principal
print('Área de um terreno')
larg = int(input('Largura do terreno em metros: '))
comp = int(input('Comprimento do terremo em metros: '))
area(larg, comp)
