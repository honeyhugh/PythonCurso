def fatorial(n, show=False):
    '''
    Calcula o fatorial de um número
    :param n: número a ser calculado o fatorial
    :param show: (opcional) mostrará o cálculo do fatorial
    :return: se show=True, mostrará o cálculo, senão apenas o resultado 
    '''
    fatorial = 1
    for c in range(n, 0, -1):
        fatorial *= c
        if show:
            if c == 1:
                print(f'{c} = ', end='')
            else:
                print(f'{c} x ', end='')
    return fatorial   
        

print(fatorial(5, True))


