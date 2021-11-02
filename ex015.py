km=float(input('Digite a quantidade de quilômetros percorridos:'))
d=int(input('Digite a quantidade de dias em que o carro foi utilizado:'))
pkm=0.15*km
pd=60*d
print('O gasto pelos {} dias foi R${:.2f} e por {:.2f}km rodados foi R${:.2f}, por tanto, o total a pagar será de R${:.2f}.'.format(d,pd,km,pkm,pd+pkm))