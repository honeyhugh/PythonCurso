from random import randint
from time import sleep
from operator import itemgetter
jogadores = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)
}
ranking = list()
for k, v in jogadores.items():
    print(f'O {k} tirou {v} no dado')
    sleep(0.5)
print('Ranking', '-=' * 15)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]}.')
print('-=' * 19)
