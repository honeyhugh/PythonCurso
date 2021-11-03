import moeda

p = float(input('Digite um valor R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}.')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}.')
print(f'Com o aumento de 10%, fica {moeda.aumento(p, 10, True)}')
print(f'Com a redução de 13%, fica {moeda.redução(p, 13, True)}.')
