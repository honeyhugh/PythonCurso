cont = soma = 0
n = int(input('Digite o número para somar (digite 999 para finalizar): '))
while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite outro número: '))  # a posição dessa linha pode adicionar o flag ou retirar
print('A soma dos {} termos digitados foi {}.'.format(cont, soma))
