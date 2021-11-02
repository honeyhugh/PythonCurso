dis = float(input('Qual foi a distância, em quilômetros, da viagem?'))
if dis <= 200:
    print('Sua viagem de {:.2f}km terá o custo de R${:.2f}. \nViagens curtas (abaixo de 200km) tem o preço de R$0,50/km'.format(dis, dis * 0.50))
else:
    print('A distância de {:.2f}km terá o custo de R${:.2f}. \nViagens longas (acima de 200km) tem o preço de R$0,45/km'.format(dis, dis * 0.45))
