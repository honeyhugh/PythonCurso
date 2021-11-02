aluno = []
lista = []
cont = 1
print('===== BOLETIM ESCOLAR =====')
while True:
    print(f'======= {cont}º Aluno(a) =======')
    aluno.append(input('Nome: ').title())
    aluno.append(float(input('Primeira Nota: ')))
    aluno.append(float(input('Segunda Nota: ')))
    aluno.append((aluno[1] + aluno[2]) / 2)
    lista.append(aluno[:])
    aluno.clear()
    cont += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Continuar? [S/N] '))[0].upper().strip()
    if 'N' in resp:
        break
print('¨' * 30)
print(f'{"Nº NOME":<15}', f'{"MÉDIA":>10}')
print('¨' * 30)
for c in lista:
    print(f'{lista.index(c)}  {c[0]:<15}', f'{c[3]:>5.1f}')
print('¨' * 60)
while True:
    n = int(input('De qual aluno você gostaria de ver as notas? (999 para interromper) '))
    if n == 999:
        break
    elif n <= len(lista) - 1:
        print(f'As respectivas notas de {lista[n][0]} foram: {lista[n][1]} e {lista[n][2]}')
        print('¨' * 60)
    else:
        print('¨' * 60)
        print('Número inválido.')
print('=' * 60)
print('Obrigada por utilizar o programa! :)')