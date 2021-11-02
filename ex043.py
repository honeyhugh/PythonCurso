peso = float(input('Seu peso em kg: '))
altura = float(input('Sua altura em metros: '))
imc = peso / altura ** 2
print('Seu Índice de Massa Corporal é {:.1f}.'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso ideal para sua altura.')
elif imc < 25:
    print('Seu peso é o ideal para sua altura.')
elif imc < 30:
    print('Você está com sobrepeso.')
elif imc < 40:
    print('Você está obeso.')
else:
    print('Você está com obesidade mórbida.')
