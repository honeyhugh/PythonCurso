pessoas = list()
idades = list()
dados = dict()
cont = 0
while True:
    resp = ' '
    cont += 1
    print(f'===== Cadastro da {cont}ª pessoa =====')
    dados['nome'] = input('Nome: ').strip().title()
    dados['idade'] = int(input('Idade: '))
    idades.append(dados['idade'])
    dados['sexo'] = ' '
    while dados['sexo'] not in 'MF':
        dados['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if dados['sexo'] not in 'MF':
            print('Erro: Digite apenas F ou M.')
    pessoas.append(dados.copy())
    dados.clear()
    while resp not in 'SN':
        resp = str(input('Continuar? [S/N] ')).strip().upper()[0]
        if resp not in 'SN':
            print('Erro: Digite apenas S ou N.')
    if resp == 'N':
        break
media = sum(idades) / len(pessoas)
print('-=' * 20)
print(f'No total, {len(pessoas)} pessoas foram cadastradas.')
print(f'A média de idade foi {media:.1f}.')
print('As mulheres cadastradas são: ', end='')
for i, p in enumerate(pessoas):
    if pessoas[i]['sexo'] == 'F':
        print(f'{pessoas[i]["nome"]}', end=' ')
print()
print(f'E as pessoas com idade acima da média são: ')
for i, p in enumerate(pessoas):
    if pessoas[i]['idade'] > media:
        print(f'{pessoas[i]["nome"]} com {pessoas[i]["idade"]} anos e sexo {pessoas[i]["sexo"]}.')
print('-=-= ENCERRADO ', '=-' * 12)
