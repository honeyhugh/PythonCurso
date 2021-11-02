casa = float(input('Qual é o valor da casa? R$'))
sal = float(input('Qual o seu salário? R$'))
tempo = int(input('Em quantos anos pretende pagar o valor da casa? '))
prest = casa / (12 * tempo)
if prest <= 30 / 100 * sal:
    print('Seu empréstimo de R${:.2f} foi aprovado com sucesso!'.format(casa))
else:
    print('Seu empréstimo foi negado. A mensalidade de R${:.2f} excedeu 30% de seu salário para o tempo disposto.'.format(prest))