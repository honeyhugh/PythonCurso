def lin(msg, cor=30):
    """
    -> Cria uma mensagem estilizada
    :param msg: Texto
    :param cor: (opcional) Troca a cor do texto
    :return: Mensagem personalizada
    """
    print(f'\033[1;{cor}m~' * (len(msg)+4))
    print(f'  {msg}')
    print('~' * (len(msg)+4))
    print('\033[m')


def ajuda(f):
    from time import sleep
    print(f'\033[1;34mAcessando o manual de {f}...\033[m')
    sleep(2)
    print('\033[1;35', end='')
    help(f)
    print('\033[m', end='')



lin('Sistema de Ajuda PyHelp', 33)
while True:
    n = input('Digite uma função ou biblioteca >')
    if n.upper() in 'FIM':
        break
    ajuda(n)
lin('Fim do programa.', 31)

# As cores n estão funcionando direito, mas o programa ta ok