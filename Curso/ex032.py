from datetime import date
ano = int(input('Digite um ano (digite 0 para saber do ano atual): '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é bissexto e eu acidentalmente achei o código'.format(ano))
else:
    print('{} não é bissexto e eu acidentalmente achei o código :('.format(ano))