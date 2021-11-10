def leiaInt(valor):
    while True:
        try:
            num = input(valor)
            return int(num)
        except (KeyboardInterrupt):
            print('\nO usuário preferiu não informar o valor.')
            return 0
        except (ValueError, TypeError):
            print('\033[0;31mErro: Digite um número inteiro válido.\033[m')


def leiaFloat(valor):
    while True:
        try:
            msg = input(valor)
            flt = msg.replace(',','.')
            return float(flt)
        except (KeyboardInterrupt):
            print('\nO usuário preferiu não informar o valor.')
            return 0
        except (ValueError, TypeError):
            print('\033[0;31mErro: Digite um número real válido.\033[m')
            

n = leiaInt('Digite um número inteiro: ')
f = leiaFloat('Digite um valor real:')
print(f'Os valores inteiro e real digitados foram {n} e {f}')