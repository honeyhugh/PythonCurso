from time import sleep
print('-' * 45)
vel = float(input('Qual foi sua velocidade, em km/h?'))
print('Processando valores...')
sleep(2)
if vel <= 80:
    print('Sua velocidade está dentro dos limites. Boa viagem!')
else:
    multa = (vel - 80) * 7
    print('Você foi multado! Sua multa por viajar a {}km/h foi R${:.2f} (Limite: 80km/h).\nMais cuidado na próxima vez.'.format(vel, multa))
print('-' * 45)
