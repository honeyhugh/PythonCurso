from ex107 import moeda

p = float(input('Digite um valor R$'))
print(f'A metade de {p} é igual a {moeda.metade(p)}.')
print(f'O dobro de {p} é {moeda.dobro(p)}.')
print(f'O aumento de 10% é {moeda.aumento(p, 10)}.')
print(f'A redução de 13% é {moeda.redução(p, 13)}.')
