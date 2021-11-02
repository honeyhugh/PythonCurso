from datetime import date
atual = date.today().year
ano = int(input('Em que ano você nasceu? '))
idade = atual - ano
if idade == 18:
    print('Está na hora do seu alistamento militar!')
elif idade > 18:
    print('Você deveria ter feito sua apresentação ao serviço militar há {} ano(s).'.format(idade - 18))
    print('Seu alistamento foi em {}'.format(atual - (idade - 18)))
else:
    print('Faltam {} ano(s) para sua apresentação ao serviço militar'.format(18 - idade))
    print('Seu alistamento  será em {}'.format(atual + (idade - 18)))
