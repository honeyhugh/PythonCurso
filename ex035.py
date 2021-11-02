from math import fabs
a = float(input('Digite o comprimento da primeira reta: '))
b = float(input('Digite o comprimento da segunda reta: '))
c = float(input('Digite o comprimento da terceira reta: '))
if fabs(b - c) < a < b + c and fabs(a - c) < b < a + c and fabs(a - b) < c < a + b:
    print('Essas retas podem sim formar um triângulo.')
else:
    print('Essas retas não podem formar um triângulo.')