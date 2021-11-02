from random import randint
lista = list()


def sorteia():
    print('Foram gerados os números: ', end='')
    lista.append(randint(0, 9))
    lista.append(randint(0, 9))
    lista.append(randint(0, 9))
    lista.append(randint(0, 9))
    lista.append(randint(0, 9))
    for v in lista:
        print(v, end=' ')
    print()
    print('-=' * 25)


def somaPar(lst):
    soma = 0
    for i in lst:
        if i % 2 == 0:
            soma += i
    print(f'E a soma dos valores pares da lista {lista} é {soma}')


sorteia()
somaPar(lista)
