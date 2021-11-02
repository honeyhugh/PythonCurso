from datetime import datetime
atual = datetime.today().year
cont = 0
velho = [0]
novo = [0]
for c in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu?'.format(cont + c)))
    if atual - ano >= 18: # considerando a maioridade 18 anos
        velho.insert(c, ano)
    else:
        novo.insert(c, ano)
maiores = len(velho[1:])
menores = len(novo[1:])
print('Dentre as 7 pessoas, {} são adultas e {} são menores de idade.'.format(maiores, menores))

# nao era bem assim, era mais simples, mas o meu ta mais completo pelo menos