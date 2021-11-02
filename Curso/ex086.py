linha1 = [[], [], []]
linha2 = [[], [], []]
linha3 = [[], [], []]
for c in range(0, 3):
    linha1[c] = int(input(f'Digite o valor para [0, {c}]: '))
for c in range(0, 3):
    linha2[c] = int(input(f'Digite o valor para [1, {c}]: '))
for c in range(0, 3):
    linha3[c] = int(input(f'Digite um valor para [2, {c}]: '))
print('=' * 30)
print(f'[{linha1[0]:^5}][{linha1[1]:^5}][{linha1[2]:^5}]')
print(f'[{linha2[0]:^5}][{linha2[1]:^5}][{linha2[2]:^5}]')
print(f'[{linha3[0]:^5}][{linha3[1]:^5}][{linha3[2]:^5}]')

# ruim.
