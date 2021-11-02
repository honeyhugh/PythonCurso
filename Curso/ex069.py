homem = maiores = mulher20 = cont = 0
sexo = escolha = ' '
while True:
    cont += 1
    print(f'==CADASTRANDO A {cont}ª PESSOA==')
    idade = int(input('Quantos anos você tem? '))
    if idade >= 18:
        maiores += 1
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Qual o seu sexo? [F/M] ')).strip().upper()[0]
    if sexo in 'F' and idade < 20:
        mulher20 += 1
    if sexo in 'M':
        homem += 1
    idade = 0
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    print('=' * 30)
    if escolha in 'N':
        break
print('No total:')
print(f'{maiores} é(são) maior(es) de idade.')
print(f'{homem} homem(ns) cadastrado(s).')
print(f'E {mulher20} mulher(es) cadastrada(s) está(ão) abaixo dos 20 anos.')
