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
    
