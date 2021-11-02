nome = input('Digite seu nome completo: ').strip().title()
print('Olá, {} {}!'.format(nome[:nome.find(' ')], nome[nome.rfind(' '):]))
