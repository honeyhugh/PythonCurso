compras = float(input('Valor total das compras: R$'))
print('''[ 1 ] À vista no dinheiro/cheque (10% de desconto)
[ 2 ] À vista no cartão (5% de desconto)
[ 3 ] 2x no cartão (valor atual)
[ 4 ] 3x ou mais no cartão (20% de juros)''')
op = int(input('Escolha uma das opções de pagamento acima: '))
if op == 1:
    novo = compras - (compras * 10 / 100)
    print('O valor da sua compra de R${:.2f} passou a custar R${:.2f}'
          ' com 10% de desconto à vista.'.format(compras, novo))
elif op == 2:
    novo = compras - (compras * 5 / 100)
    print('O valor da sua compra de R${:.2f} passou a custar R${:.2f}'
          ' com 5% de desconto à vista no cartão.'.format(compras, novo))
elif op == 3:
    print('O valor de sua compra de R${:.2f} sairá de 2x de R${:.2f}.'.format(compras, compras / 2))
elif op == 4:
    n = int(input('De quantas vezes você quer parcelar?'))
    juros = (compras + (20 / 100 * compras)) / n
    print('Parcelando suas compras de R${:.2f} em {}x,'
          ' o valor mensal será de R${:.2f} com 20% de juros.'.format(compras, n, juros))
else:
    print('Opção inválida. Tente novamente.')
