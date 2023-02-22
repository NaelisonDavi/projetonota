import sys

def materias(NOME_DO_ALUNO, NOME_DA_MATERIA, NOTA_DA_MATERIA):
    while NOME_DO_ALUNO != 'sair':
        NOME_DO_ALUNO = str(input('Digite o nome do aluno: '))

        if NOME_DO_ALUNO == 'sair':
            break

        NOME_DA_MATERIA = str(input('Digite o nome da matéria: '))

        if NOME_DA_MATERIA == 'sair':
            break

        NOTA_DA_MATERIA = float(input('Digite a nota da matéria: '))

        if NOTA_DA_MATERIA == 'sair':
            break
            
        MATERIA[NOME_DO_ALUNO] = [NOME_DA_MATERIA, NOTA_DA_MATERIA]

    for NOME_DO_ALUNO in MATERIA.keys():

        MAIOR_NOTA = maior_nota('maior_nota_atual', 'nova_nota')
        if NOTA_DA_MATERIA == MAIOR_NOTA:
            NOTA_DA_MATERIA = NOME_DO_ALUNO

        MENOR_NOTA_MATERIA = menor_nota('menor_nota_atual', 'nova_nota')
        if NOTA_DA_MATERIA == MENOR_NOTA_MATERIA:
            NOTA_DA_MATERIA = NOME_DO_ALUNO

def maior_nota(maior_nota_atual:float, nova_nota:float):
    if nova_nota > maior_nota_atual:
        return nova_nota
    return maior_nota_atual

def menor_nota(menor_nota_atual:float, nova_nota:float):
    if nova_nota < menor_nota_atual:
        return nova_nota
    return menor_nota_atual

if __name__ == '__main__':

    MAIOR_NOTA = 0
    MENOR_NOTA = sys.maxsize
    MATERIA = dict()

materias('NOME_DO_ALUNO', 'NOME_DA_MATERIA', 'NOTA_DA_MATERIA')
print(MATERIA)
print(MAIOR_NOTA)
print(MENOR_NOTA)