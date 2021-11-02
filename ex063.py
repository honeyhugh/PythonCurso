print('==Sequência de Fibonacci==')
n = int(input('Quantos termos quer ver? '))
cont = 0
termo1 = 1
termo2 = 0
atual = 0
while cont != n:
    cont += 1
    print('{} '.format(termo2), end=' ')
    atual = termo1 + termo2
    termo1 = termo2
    termo2 = atual
