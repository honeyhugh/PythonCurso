from random import randint
from time import sleep
e = randint(0, 5)
print('=:=' * 12)
num = int(input('Dgite um número entre 0 e 5: '))
print('PROCESSANDO...')
sleep(3)
if num == e:
    print('Parabéns! Eu pensei no {} também.'.format(num))
else:
    print('Ops, não pensei no {}. A resposta era {}.'.format(num, e))
