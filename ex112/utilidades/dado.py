def leiaDinheiro(msg):
    while True:
        n = str(input(msg)).strip().replace(',','.')
        if n.isalpha() or n == '':
            print(f'ERRO: digite um valor monetário')
        else:
            return float(n) 

