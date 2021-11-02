from datetime import datetime
pessoas = dict()
pessoas['Nome'] = input('Seu Nome: ').strip().title()
ano = int(input('Ano de nascimento: '))
pessoas['Idade'] = datetime.today().year - ano
pessoas['CTPS'] = int(input('Número da CTPS (se não tiver, digite 0): '))
if pessoas['CTPS'] == 0:
    print('=' * 30)
    for k, v in pessoas.items():
        print(f'{k}: {v}')
    print('Situação: Não possui carteira de trabalho.')
elif pessoas['CTPS'] > 0:
    pessoas['Ano de Contratação'] = int(input('Ano de contratação: '))
    apos = (pessoas['Ano de Contratação'] + 35) - ano
    pessoas['Salário'] = int(input('Salário (sem os centavos): R$'))
    print('=' * 30)
    for k, v in pessoas.items():
        print(f'{k}: {v}')
    print(f'A idade com que irá se aposentar será {apos}.')
