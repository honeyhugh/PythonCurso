nome = str(input('Digite seu nome: ').strip().upper())
print('O nome "{}" possui "Silva"? {}'.format(nome.title(), 'SILVA' in nome))