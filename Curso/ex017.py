from math import hypot
ad=float(input('Digite o comprimento do cateto adjacente: '))
op=float(input('Digite o comprimento do cateto oposto: '))
hip=hypot(op,ad)
print('A hipotenusa desse triângulo retângulo é {:.2f}'.format(hip))