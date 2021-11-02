def ficha(nome='', gols=''):
    if nome == '':
        nome = 'desconhecido'
    if gols.isnumeric():
        int(gols)
    else:
        gols = 0
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'


n = input('Nome do jogador: ').strip()
g = input('Quantidade de gols: ')
print(ficha(n, g))
