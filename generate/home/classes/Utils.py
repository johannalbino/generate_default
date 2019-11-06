
def departament(id):
    if id == 1:
        return 'FISCAL'
    elif id == 2:
        return 'CONTÁBIL'
    elif id == 3:
        return 'MATERIAIS'
    elif id == 4:
        return 'FINANCEIRO'
    elif id == 5:
        return 'NFCE'
    elif id == 6:
        return 'GERAL'
    elif id == 7:
        return 'DIRETÓRIOS PADRÕES'


def departament_name(departament):
    if departament == 'Fiscal':
        return 1
    elif departament == 'Contábil':
        return 2
    elif departament == 'Materiais':
        return 3
    elif departament == 'Financeiro':
        return 4
    elif departament == 'NFCE':
        return 5
    elif departament == 'Geral':
        return 6
    elif departament == 'Diretorio':
        return 7

