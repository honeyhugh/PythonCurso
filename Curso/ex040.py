print('°' * 21)
print('\033[1;38mANALISADOR DE MÉDIAS\033[m')
print('°' * 21)
n1 = float(input('- Primeira nota: '))
n2 = float(input('- Segunda nota: '))
n3 = float(input('- Terceira nota: '))
n4 = float(input('- Quarta nota: '))
media = (n1 + n2 + n3 + n4) / 4
if media < 5:
    print('Você foi \033[1;31mREPROVADO\033[m.')
    print('Sua média foi {}. Você não alcançou 5 pontos para fazer a recuperação.'.format(media))
elif 5 <= media < 6.9:
    print('Você está de \033[1;33mRUCUPERAÇÃO\033[m.')
    print('Sua média foi de {}. Você não alcançou 7 pontos para passar direto.'.format(media))
else:
    print('Parabéns, Você foi \033[1;32mAPROVADO\033[m!')
    print('Sua média foi {}.'.format(media))
