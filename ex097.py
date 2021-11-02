from math import trunc
def escreva(msg):
    c = trunc(len(msg)/2)
    print(f'{"-=":^}' * (c + 2))
    print(f'  {msg}')
    print(f'{"-=":^}' * (c + 2))


# Programa Principal
n = input('Escreva uma mensagem: ')
escreva(n)
