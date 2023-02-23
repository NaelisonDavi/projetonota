import sys

with open('código da turma.txt', 'w') as arquivo:

    def criador_de_dicionario(NOME_DO_ALUNO:int, NOME_DA_MATERIA:int, NOTA_DO_ALUNO:float):
        while NOME_DO_ALUNO != 'sair': 

            NOME_DO_ALUNO = str(input('Digite o nome do aluno(a): \n'))
            if NOME_DO_ALUNO == 'sair':
                break

            NOME_DA_MATERIA = str(input('Insira o nome da matéria: \n'))
            if NOME_DA_MATERIA == 'sair':
                break

            NOTA_DO_ALUNO = float(input('Insira uma nota: \n'))
            if NOTA_DO_ALUNO == 'sair':
                break

            TODAS_AS_NOTAS = {'NOME_DO_ALUNO': {'NOME_DA_MATERIA': 'NOTA_DO_ALUNO'}}

        return TODAS_AS_NOTAS
        
    def calcular_maior_nota(MAIOR_NOTA_ATUAL:float, NOTA_DO_ALUNO:float):
        if NOTA_DO_ALUNO in TODAS_AS_NOTAS.items() > MAIOR_NOTA_ATUAL:
            MAIOR_NOTA_ATUAL = NOTA_DO_ALUNO
            return MAIOR_NOTA_ATUAL
        return NOTA_DO_ALUNO

    def calcular_menor_nota(MENOR_NOTA_ATUAL:float, NOTA_DO_ALUNO:float):
        if NOTA_DO_ALUNO in TODAS_AS_NOTAS.items() < MENOR_NOTA_ATUAL:
            MENOR_NOTA_ATUAL = NOTA_DO_ALUNO
            return MENOR_NOTA_ATUAL
        return NOTA_DO_ALUNO

    if __name__ == '__main__':

        CODIGO = str(input('Digite o código da turma(a): \n'))
        MAIOR_NOTA_ATUAL = 0
        MENOR_NOTA_ATUAL = sys.maxsize
        TODAS_AS_NOTAS = dict()

criador_de_dicionario('NOME_DO_ALUNO', 'NOME_DA_MATERIA', 'NOTA_DO_ALUNO')
calcular_maior_nota('MAIOR_NOTA_ATUAL', 'NOTA_DO_ALUNO')
print(type(TODAS_AS_NOTAS))