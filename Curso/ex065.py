n = cont = soma = media = maior = menor = 0
escolha = 's'
while escolha in 'SIMsim':
    n = float(input('Digite um número: '))
    if cont == 0:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    soma += n
    cont += 1
    escolha = input('Quer continuar? [S/N] ').strip()
media = soma / cont
print('A média entre os {} valores foi {:.2f}'.format(cont, media))
print('O maior valor foi {:.1f} e o menor foi {:.1f}.'.format(maior, menor))
