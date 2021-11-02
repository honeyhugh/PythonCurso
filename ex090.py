aluno = dict()
aluno['Nome'] = input('Nome do(a) Aluno(a): ').strip().title()
aluno['Média'] = float(input(f'Média Final de {aluno["Nome"]}: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado(a)'
elif aluno['Média'] >= 5:
    aluno['Situação'] = 'de Recuperação'
else:
    aluno['Situação'] = 'Reprovado(a)'
print('- -' * 15)
for k, v in aluno.items():
    print(f'{k} é {v}.')
