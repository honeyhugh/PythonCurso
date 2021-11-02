t = 'pedra', 'papel', 'tesoura', 'garrafa', 'mouse', 'livro'
for pos in range(0, len(t)):
    print(f'\nNa palavra {t[pos].upper()} as vogais são: ', end='')
    for v in t[pos]:
        if v in 'aeiou':
            print(v, end=' ')
