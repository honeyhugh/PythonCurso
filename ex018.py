from math import sin,cos,tan,radians
an=float(input('Digite um ângulo em graus:'))
sen=sin(radians(an))
coss=cos(radians(an))
tang=tan(radians(an))
print('Seno: {:.2f} \nCosseno: {:.2f} \nTangente: {:.2f}'.format(sen,coss,tang))