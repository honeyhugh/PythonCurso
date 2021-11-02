num = range(0, 21)
extenso = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',\
          'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
while True:
    n = int(input('Digite um número entre 0 e 20:'))
    escolha = ' '
    while n not in num:
        print('Tente Novamente.')
        n = int(input('Digite um número de 0 a 20:'))
    print(f'O número {n} por extenso é {extenso[n]}')
    while escolha not in 'NS':
        escolha = str((input('Quer continuar? [S/N] '))).strip().upper()[0]
    if escolha in 'N':
        break
print('Programa Finalizado. Obrigada :)')
