import sys


def criador_de_dicionario():

    nome_do_aluno = ''
    todas_as_notas = dict()

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

        todas_as_notas[(nome_do_aluno, nome_da_materia)] = nota_do_aluno

    return todas_as_notas

def calcular_maior_nota(nova_nota:float, todas_as_materias:dict, maior_atual:float):
    for nova_nota in todas_as_materias.items():
        if nova_nota > maior_atual:
            maior_atual = nova_nota
            return maior_atual
        return nova_nota

    
if __name__ == '__main__':

    codigo = str(input('Digite o código da turma(a): \n'))
    maior_nota_atual = 0
    menor_nota_atual = sys.maxsize
    resultado_final = criador_de_dicionario()
    print(resultado_final)
  #  resultado_final_maior = calcular_maior_nota('nota_do_aluno', 'todas_as_materias', 'maior_nota_atual')
