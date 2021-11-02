from random import choice
p1 = input('Digite o nome do(a) primeiro(a) aluno(a): ')
p2 = input('Digite o nome do(a) segundo(a) aluno(a): ')
p3 = input('Digite o nome do(a) terceiro(a) aluno(a): ')
p4 = input('Digite o nome do(a) quarto(a) aluno(a): ')
r = choice([p1,p2,p3,p4])
print('O(A) aluno(a) sorteado(a) foi {}!'.format(r))
