from time import sleep


def maior(* valores):
    if len(valores) == 0:
        maior = 0
    else:
        maior = max(valores) 
    print('Dos valores digitados ', end='')
    for c in valores:
        print(c, end=' ', flush=True)
        sleep(0.5)
    print()
    print(f'Foram informados {len(valores)} valores.')
    print(f'O maior valor foi: {maior}')
    print('-=' * 25)


maior(0)
maior(0, 1, -1)
maior()
maior(10, 9, 0, 12)

