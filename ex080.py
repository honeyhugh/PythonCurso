
#programa ainda não finalizado

n = []
for c in range(0, 5):
    valor = int(input('Digite um valor: '))
    if c == 0 or valor > n[-1]:
        n.append(valor)
        print('Valor adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(n):
            if valor <= n[pos]: #TypeError
                n.insert(pos, n)
                print(f'Valor adicionado na posição {pos}.')
            break
        pos += 1
print(n)
