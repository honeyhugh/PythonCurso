n = int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')),\
    int(input('Digite um número: '))

print(f'Os números digitados foram: {n}')
print(f'O valor 9 aparece {n.count(9)} vezes')
if 3 in n:
    print(f'O número 3 foi digitado na {n.index(3) + 1}ª posição')
else:
    print('O número 3 foi digitado em nenhuma posição')
print('Os números pares digitados foram: ', end='')
for num in n:
    if num % 2 == 0:
        print(num, end=' ')
