print('Detector de palíndromo')
frase = input('Digite a frase: ').upper().strip().replace(' ', '')
pali = ' '.join(frase).split()
inverso = ''
for letra in range(len(pali) - 1, -1, -1):
    inverso += pali[letra]
if frase == inverso:
    print('{} é um palindromo'.format(frase))
else:
    print('{} não é um palindromo'.format(frase))
