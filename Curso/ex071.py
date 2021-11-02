from time import sleep
cont50 = cont20 = cont10 = cont1 = 0
print('{:=^25}'.format('BOIOLA BANK'))
nome = input('Digite seu primeiro nome, por favor: ')
print(f'Bom dia, {nome}!')
valor = int(input('Qual quantia gostaria de retirar hoje? R$'))
print('PROCESSANDO...')
sleep(1)
montante = valor
while True:
    if montante >= valor:
        cont50 += 1
        montante -= 50
    else:
        break
while True:
    if montante >= 20:
        cont20 += 1
        montante -= 20
    else:
        break
while True:
    if montante >= 10:
        cont10 += 1
        montante -= 10
    else:
        break
print('=' * 25)
print('Total retirado:')
print(f'{cont50} cédulas de R$50.')
print(f'{cont20} cédulas de R$20.')
print(f'{cont10} cédulas de R$10.')
print(f'{montante} cédulas de R$1')
print('Obrigada por utilizar o BB! tenha um bom dia. :)')


