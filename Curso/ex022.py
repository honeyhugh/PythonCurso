nome = str(input('Digite seu nome: ')).strip()
spt = stp.split()
print('O nome, em maiúsculas, é: ', stp.upper())
print('O nome, em minúsculas, é: ', stp.lower())
print('A soma de todas as letras é: ', len(nome) - nome.count(' '), '.')
print('A soma de todas as letras do primeiro nome é: ', len(spt[0]), '.')

# Na linha 6 ele utilizou o ' '.find(nome) para achar o primeiro espaço, ou seja, o número retornado pelo join seria
# a quantidade de caracteres do primeiro nome

