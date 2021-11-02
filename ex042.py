from math import fabs
a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o terceiro segmento: '))
fator = fabs(b - c) < a < b + c and fabs(a - c) < b < a + c and fabs(a - b) < c < a + b
if fator:
    print('Os três segmentos podem sim formar um triângulo.')
    if a != b and b != c and a != c:
        print('E esse triângulo é do tipo ESCALENO.')
    elif a == b and b == c:
        print('E esse triângulo é do tipo EQUILÁTERO.')
    elif a or b == c or a == b:
        print('E esse triângulo é do tipo ISÓSCELES.')
else:
    print('Os três segmentos não podem formar um triângulo.')