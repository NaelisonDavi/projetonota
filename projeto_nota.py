import sys

with open('código da turma.txt', 'w') as arquivo:

    def criador_de_dicionario(nome_do_aluno:int, nome_da_materia:int, nota_do_aluno:float):
        while nome_do_aluno != 'sair': 

            nome_do_aluno = str(input('Digite o nome do aluno(a): \n'))
            if nome_do_aluno == 'sair':
                break

            nome_da_materia = str(input('Insira o nome da matéria: \n'))
            if nome_da_materia == 'sair':
                break

            nota_do_aluno = float(input('Insira uma nota: \n'))
            if nota_do_aluno == 'sair':
                break

            TODAS_AS_NOTAS[(nome_do_aluno, nome_da_materia)] = nota_do_aluno

        return TODAS_AS_NOTAS
        
    def calcular_maior_nota(maior_nota_atual:float, nota_do_aluno:float):
        if nota_do_aluno in TODAS_AS_NOTAS.items() > maior_nota_atual:
            maior_nota_atual = nota_do_aluno
            return maior_nota_atual
        return nota_do_aluno

    def calcular_menor_nota(menor_nota_atual:float, nota_do_aluno:float):
        if nota_do_aluno in TODAS_AS_NOTAS.items() < menor_nota_atual:
            menor_nota_atual = nota_do_aluno
            return menor_nota_atual
        return nota_do_aluno

    if __name__ == '__main__':

        CODIGO = str(input('Digite o código da turma(a): \n'))
        MAIOR_NOTA_ATUAL = 0
        MENOR_NOTA_ATUAL = sys.maxsize
        TODAS_AS_NOTAS = dict()

criador_de_dicionario('NOME_DO_ALUNO', 'NOME_DA_MATERIA', 'NOTA_DO_ALUNO')
print(TODAS_AS_NOTAS)