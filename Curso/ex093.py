jogador = dict()
jogador['Nome'] = input('Nome do jogador: ').strip().title()
jogador['Partidas'] = int(input(f'Quantidade de partidas que {jogador["Nome"]} jogou: '))
gols = list()
for p in range(1, jogador['Partidas'] + 1):
    gols.append(int(input(f'Gols feitos na {p}ª partida: ')))
jogador['Gols'] = gols.copy()
jogador['Total de Gols'] = sum(gols)
print('-=' * 20)
print(jogador)
print('-=' * 20)
for k, v in jogador.items():
    print(f'{k}: {v}')
print('-=' * 20)
print(f'O jogador {jogador["Nome"]} jogou {jogador["Partidas"]} partidas.')
for v in range(1, jogador['Partidas'] + 1):
    print(f'=> Na {v}ª partida, fez {jogador["Gols"][v - 1]} gol(s)')
print(f'E o total de gols foi {jogador["Total de Gols"]}.')
