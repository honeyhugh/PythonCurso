def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')


def metade(valor=0, format=False):
    res = valor / 2
    if format:
        return moeda(res)
    else:
        return res


def dobro(valor=0, format=False):
    res = valor * 2
    if format:
        return moeda(res)
    else:
        return res


def aumento(valor=0, porcento=0, format=False):
    res = valor + valor * (porcento / 100)
    if format:
        return moeda(res)
    else:
        return res


def redução(valor=0, porcento=0, format=False):
    res = valor - valor * (porcento / 100) 
    if format:
        return moeda(res)
    else:     
        return res
    

def resumo(valor=0, aum=10, red=5):
    print('-=' * 21)
    print(f'RESUMO DO VALOR'.center(40))
    print('-=' * 21)
    print(f' Preço analisado: \t\t{moeda(valor)}')
    print(f' Dobro do preço: \t\t{dobro(valor, True)}')
    print(f' Com o aumento de {aum}%: \t\t{aumento(valor, aum, True)}')
    print(f' Com a redução de {red}%: \t\t{redução(valor, red, True)}')
    print('-=' * 21)