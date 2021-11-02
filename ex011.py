l=float(input('Insira a largura da parede: '))
a=float(input('Insira a altura da parede: '))
m=l*a
print('As dimensões dessa parede são {:.2f}x{:.2f} e sua área é {:.2f}m².'.format(l,a,m))
lit=m/2
print('Para pintar toda a parede, serão necessários {:.2f}l de tinta.'.format(lit))