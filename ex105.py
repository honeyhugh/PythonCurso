def notas(*n, sit=False):
    '''
    - Função para analisar notas e a situação de vários alunos.
    :param n: Recebe várias notas de alunos;
    :param sit: (opcional) Situação da turma;
    :return: Um dicionário com as informações da turma.
    '''
    turma = dict()
    turma['total'] = len(n)
    turma['maior'] = max(n)
    turma['menor'] = min(n)
    turma['media'] = sum(n) / len(n)
    if sit:
        if turma['media'] <= 5:
            turma['sit'] = 'Ruim'
        elif turma['media'] <= 7:
            turma['sit'] = 'Razoável'
        else: 
            turma['sit'] = 'Boa'
        return turma
    else:
        return turma


print(notas(5.5, 9, 6.5, 8, sit=True))
