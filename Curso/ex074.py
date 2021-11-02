from random import randint
num = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)
maior = menor = num[0]
for c in num: # Maneira tradicional
    if c >= maior:
        maior = c
    if c < menor:
        menor = c
print(num)
print(f'Na sequência acima, o número {maior} é o maior e o {menor} é o menor.')

# Maneira mais simplificada
# com coleções, é possivel usar os métodos 'max()' e 'min()' para achar o maior e menor valor
# print(f'O maior valor foi {max(num)} e o menor foi {min(num)}')
