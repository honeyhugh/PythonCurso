soma = cont = n = 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'A soma dos {cont} números digitados foi {soma}.')
