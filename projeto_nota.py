import sys

def criador_de_dicionario():

    nome_do_aluno = ''
    todas_as_notas = dict()
    quantidade_de_materias = int(input('digite a quantidade de matérias'))

    while nome_do_aluno != 'sair': 

        nome_do_aluno = str(input('Digite o nome do aluno(a): \n'))
        if nome_do_aluno == 'sair':
            break

        todas_as_notas[nome_do_aluno] = list()

        for _ in range(quantidade_de_materias):

            nota_do_aluno = input('Insira uma nota: \n')
            if nota_do_aluno == 'sair':
                break
            nota_do_aluno = float(nota_do_aluno)
            todas_as_notas[nome_do_aluno].append(nota_do_aluno)
    return todas_as_notas

def calcular_maior_nota(nova_nota:float, todas_as_materias:dict, maior_atual:float):
    for nova_nota in todas_as_materias.items():
        if nova_nota > maior_atual:
            maior_atual = nova_nota
            return maior_atual
        return nova_nota
    
if __name__ == '__main__':

    maior_nota_atual = 0
    menor_nota_atual = sys.maxsize
    resultado_final = criador_de_dicionario()
    print(resultado_final)
  #  resultado_final_maior = calcular_maior_nota('nota_do_aluno', 'todas_as_materias', 'maior_nota_atual')
