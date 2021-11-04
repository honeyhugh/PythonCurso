import moeda

p = float(input('Digite um valor R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}.')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}.')
print(f'Com o aumento de 10%, fica {moeda.moeda(moeda.aumento(p, 10))}')
print(f'Com a redução de 13%, fica {moeda.moeda(moeda.redução(p, 13))}.')

