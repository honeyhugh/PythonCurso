time = list()
jogador = dict()
gols = list()
while True:
    resp = ' '
    print('-=' * 30)
    jogador['Nome'] = input('Nome do jogador: ').strip().title()
    jogador['Partidas'] = int(input(f'Quantidade de partidas que {jogador["Nome"]} jogou: '))
    for p in range(1, jogador['Partidas'] + 1):
        gols.append(int(input(f'Gols feitos na {p}ª partida: ')))
    jogador['Gols'] = gols.copy()
    jogador['Total de Gols'] = sum(gols)
    time.append(jogador.copy())
    jogador.clear()
    gols.clear()
    while resp not in 'SN':
        resp = str(input('Adicionar outro jogador? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 30)
print(f'{"cód.":<5} {"Nome":<16} {"Gols":<15} {"Total":<5}')
for i, v in enumerate(time):
    print(f'{i:<5} {time[i]["Nome"]:<16} {str(time[i]["Gols"]):<15} {time[i]["Total de Gols"]:<5}')
while True:
    print('-=' * 30)
    n = int(input('De qual jogador gostaria de saber os detalhes? (999 para parar) '))
    if n == 999:
        break
    elif n >= len(time):
        print(f'O código {n} não pertence a nenhum jogador. Tente novamente.')
    else:
        print(f'===LEVANTAMENTO DO JOGADOR {time[n]["Nome"]}===.')
        for v in range(1, time[n]['Partidas'] + 1):
            print(f'=> Na {v}ª partida, fez {time[n]["Gols"][v - 1]} gol(s)')
        print(f'E o total de gols foi {time[n]["Total de Gols"]}.')
print('-=' * 30)
print('Programa finalizado. Volte Sempre.')
