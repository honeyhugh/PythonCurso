from random import randint
from time import sleep
print('\033[1;33m{:=^30}\033[m'.format(' JOKENPÔ '))
print('''\033[;37m[ 0 ] Pedra\033[m
\033[;38m[ 1 ] Papel\033[m
\033[;31m[ 2 ] Tesoura\033[m''')
escolha = ['\033[1;37mpedra\033[m', '\033[1;38mpapel\033[m', '\033[1;31mtesoura\033[m']
n = int(input('\033[1;33mEscolha uma opção:\033[m'))
pc = randint(0, 2)

print('\033[1;33mJO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!\033[m')

if n == pc:
    print('Sua escolha: {}.'.format(escolha[n]))
    print('PC: {}.'.format(escolha[pc]))
    print('Parece que a gente escolheu o mesmo! :0 \nVamos de novo.')
elif n == 0 and pc == 1:
    print('Sua escolha: {}.'.format(escolha[n]))
    print('PC: {}.'.format(escolha[pc]))
    print('Ha! Parece que eu ganhei :>')
elif n == 0 and pc == 2:
    print('Sua escolha: {}.'.format(escolha[n]))
    print('PC: {}.'.format(escolha[pc]))
    print('OK, você ganhou dessa vez :/')
elif n == 1 and pc == 0:
    print('Sua escolha: {}.'.format(escolha[n]))
    print('PC: {}.'.format(escolha[pc]))
    print('OK, você ganhou dessa vez :/')
elif n == 1 and pc == 2:
    print('Sua escolha: {}.'.format(escolha[n]))
    print('PC: {}.'.format(escolha[pc]))
    print('Ha! Parece que eu ganhei :>')
elif n == 2 and pc == 0:
    print('Sua escolha: {}.'.format(escolha[n]))
    print('PC: {}.'.format(escolha[pc]))
    print('Ha! Parece que eu ganhei :>')
elif n == 2 and pc == 1:
    print('Sua escolha: {}.'.format(escolha[n]))
    print('PC: {}.'.format(escolha[pc]))
    print('Ok, você ganhou dessa vez :/')
else:
    print('Ops, essa opção é inválida. \nLembre-se: \nO número 0 é para Pedra \nO número 1 é para Papel \nO número 2'
          ' é para Tesoura')
