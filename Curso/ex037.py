print('=+=' * 20)
print('CONVERSOR DE BASES NUMÉRICAS')
print('=+=' * 20)
n = int(input('Digite um número: '))
print('''Escolha a base  para a conversão 
[ 1 ] Base Binária
[ 2 ] Base Octal
[ 3 ] Base Hexadecimal''')
op = int(input('Sua opção: '))
if op == 1:
    print('{} em base binária é {}.'.format(n, bin(n)[2:]))
elif op == 2:
    print('{} em base octal é {}'.format(n, oct(n)[2:]))
elif op == 3:
    print('{} em base hexadecimal é {}.'.format(n, hex(n)[2:]))
else:
    print('Opção {} inválida. Tente novamente.'.format(n))
