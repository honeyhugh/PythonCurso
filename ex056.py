idadevelho = 0
nomevelho = ['']
mulherveia = 0
idades = list()
for p in range(1, 5):
    print('{}ª pessoa:'.format(p))
    nome = input('Qual o seu nome? ').strip()
    sexo = str(input('Qual o seu sexo? (F/M) ')).strip().upper()[0]
    idade = int(input('Qual a sua idade? '))
    idades.append(idade)
    if sexo == 'M' and idade > idadevelho:
        idadevelho = idade
        nomevelho = nome
    if sexo == 'F' and idade <= 19:
        mulherveia += 1
media = sum(idades) / 4
print('A média de idade do grupo foi {:.1f} anos.\n'
      '{} é o homem mais velho com {} anos.\n'
      'E há {} mulher(es) abaixo dos 20 anos.'.format(media, nomevelho.title(), idadevelho, mulherveia))
