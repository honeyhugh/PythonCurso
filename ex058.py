from random import randint
pc = randint(0, 10)
cont = 0
print('Pensei em um número entre 0 e 10.')
n = int(input('Você consegue adivinhar? :> Então diga: '))
while pc != n:
    if pc > n:
        print('Maior...')
    elif pc < n:
        print('Menor...')
    n = int(input('Tente novamente: '))
    cont += 1
if cont == 0:
    print('PARABENS! Você acertou de primeira e não precisou repetir :O')
else:
    print('Aí simm, pensei no {} também, só que você tentou {} vez(es) até acertar.'.format(pc, cont + 1))
