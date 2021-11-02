from datetime import date

atual = date.today().year
ano = int(input('Em que ano você nasceu? '))
idade = atual - ano
if atual - ano <= 9:
    print('Sua idade é {} anos e sua categoria é MIRIM.'.format(idade))
# Se o filtro passou pela linha 5 e constatou que o usuario não é menor ou tem 9 anos
# "10 <=" não será necessário e assim por diante
elif 10 <= atual - ano <= 14:
    print('Sua idade é {} anos e sua categoria é INFANTIL.'.format(idade))
elif 15 <= atual - ano <= 19:
    print('Sua idade é {} anos e sua categoria é JÚNIOR.'.format(idade))
elif 20 <= atual - ano <= 25:
    print('Sua idade é {} anos e sua categoria é SÊNIOR.'.format(idade))
elif atual - ano > 25:
    print('Sua idade é {} anos  e sua categoria é MASTER.'.format(idade))
