bruto = float(input('Qual o seu salário? R$'))
if bruto <= 1250:
    sal = (bruto * 15/100) + bruto
    pc = 15
else:
    sal = (bruto * 10/100) + bruto
    pc = 10
print('Seu salário de R${:.2f} teve o aumento de {}% e ficou R${:.2f}.'.format(bruto, pc, sal))