def voto(ano):
    '''
    Analisador de situação eleitoral
    :param ano: Ano de nascimento do usuário
    :return: A idade e a situação eleitoral
    '''
    from datetime import datetime
    idade = datetime.now().year - ano
    if idade < 16:
        voto = 'NEGADO'
    elif 16 <= idade < 18 or idade >= 65:
        voto = 'OPCIONAL'
    else:
        voto = 'OBRIGATÓRIO'
    return f'Com {idade} anos, o voto é {voto}.'



n = int(input('Em que ano você nasceu? '))
print(voto(n))
