def leiaInt(valor):
    while True:
        num = input(valor)
        if str(num).isnumeric():
            return int(num)
            break
        else:
            print('\033[0;31mErro: Digite um valor númerico.\033[m')
            

n = leiaInt('Digite um número: ')
print(n)