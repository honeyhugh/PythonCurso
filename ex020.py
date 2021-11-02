import random
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
l = [n1, n2, n3, n4]
random.shuffle(l)
print('A nova ordem será')
print(l)