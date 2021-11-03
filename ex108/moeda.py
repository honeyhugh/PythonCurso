def metade(valor=0):
    res = valor / 2
    return res


def dobro(valor=0):
    res = valor * 2
    return res


def aumento(valor=0, porcento=0):
    res = valor + valor * (porcento / 100)
    return res


def redução(valor=0, porcento=0):
    res = valor - valor * (porcento / 100) 
    return res


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')


