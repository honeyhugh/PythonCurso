escolha = 0
maior = 0
n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
print('[ 1 ] Somar \n'
      '[ 2 ] Multiplicar \n'
      '[ 3 ] Maior \n'
      '[ 4 ] Novos números \n'
      '[ 5 ] Fechar Programa')
while escolha != 5:
    escolha = int(input('O que deseja fazer? '))
    if escolha == 1:
        print('A soma entre {:.1f} e {:.1f} é {:.1f}.'.format(n1, n2, n1 + n2))
        print('==*==' * 10)
    elif escolha == 2:
        print('A multiplicação entre {:.1f} e {:.1f} é {:.1f}.'.format(n1, n2, n1 * n2))
        print('==*==' * 10)
    elif escolha == 3:
        if n1 > n2:
            maior = n1
        elif n2 > n1:
            maior = n2
        print('Entre {:.1f} e {:.1f}, o maior número é o {:.1f}.'.format(n1, n2, maior))
        print('==*==' * 10)
    elif escolha == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
        print('==*==' * 10)
    elif escolha == 5:
        print('==*==' * 10)
    else:
        print('Opção inválida, tente novamente.')
        print('==*==' * 10)
print('Programa finalizado. Obrigada por utilizar!')
