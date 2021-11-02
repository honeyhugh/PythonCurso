sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, digite novamente: ')).strip().upper()[0]
print('Sexo valido, obrigada')
