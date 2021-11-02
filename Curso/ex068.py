from random import randint
print('==PAR OU ÍMPAR==')
cont = 0
while True:
    usuario = 'false'
    pc = randint(0, 10)
    soma = pc
    n = -1
    while n not in range(0, 11):
        n = int(input('Digite um valor de 0 a 10: '))
    soma += n
    while usuario not in 'PpIi':
        usuario = str(input('Escolha par ou ímpar: [P/I] ').strip())[0]
    print(f'O computador jogou {pc} e a soma foi {soma}')
    if usuario in 'Pp' and soma % 2 == 0:
        cont += 1
        print(f'V0CÊ GANHOU, parabéns!')
    elif usuario in 'Ii' and soma % 2 != 0:
        cont += 1
        print('V0CÊ GANHOU, parabéns!')
    else:
        print('COMPUTADOR GANHOU!')
        break
print(f'GAME OVER. Você perdeu com {cont} vitória(s) consecutivas.')
