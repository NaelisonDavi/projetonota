import sys

with open('código da turma.txt', 'w') as arquivo:

    def maior_nota(maior_atual:float, num:float):
        if num > maior_atual:
            return num
        return maior_atual

    def menor_nota(menor_atual:float, num:float):
        if num < menor_atual:
            return num
        return menor_atual

    if __name__ == '__main__':

        codigo = str(input('Digite o código da turma(a): \n'))
        nome = 0
        maior_mat = 0
        maior_por = 0
        maior_his = 0
        menor_mat = sys.maxsize
        menor_por = sys.maxsize
        menor_his = sys.maxsize
        nota = dict()

        while nome != 'sair': 
            nome = str(input('Digite o nome do aluno(a): \n'))
            
            if nome == 'sair':
                break

            mat = int(input('Nota de matemática: \n'))
            por = int(input('Nota de português: \n'))
            his = int(input('Nota de história: \n'))
            nota[nome] = [mat, por, his]

        for (nome_do_aluno, notas_do_aluno) in nota.items():

            nota_mat = notas_do_aluno[0]
            nota_por = notas_do_aluno[1]
            nota_his = notas_do_aluno[2]

            maior_mat = maior_nota(nota_mat, maior_mat)
            if nota_mat == maior_mat:
                maior_nota_aluno_mat = nome_do_aluno

            maior_por = maior_nota(nota_por, maior_por)
            if nota_por == maior_por:
                maior_nota_aluno_por = nome_do_aluno

            maior_his = maior_nota(nota_his, maior_his)
            if nota_his == maior_his:
                maior_nota_aluno_his = nome_do_aluno

            menor_mat = menor_nota(nota_mat, menor_mat)
            if nota_mat == menor_mat:
                menor_nota_aluno_mat = nome_do_aluno

            menor_por = menor_nota(nota_por, menor_por)
            if nota_por == menor_por:
                menor_nota_aluno_por = nome_do_aluno

            menor_his = menor_nota(nota_his, menor_his)
            if nota_his == menor_his:
                menor_nota_aluno_his = nome_do_aluno


    print(f'A maior nota de matemática foi de {maior_nota_aluno_mat}: {maior_mat}, e a menor foi de {menor_nota_aluno_mat}: {menor_mat}', file=arquivo)
    print(f'A maior nota de português foi de {maior_nota_aluno_por}: {maior_por} e a menor {menor_nota_aluno_por}: {menor_por}', file=arquivo)
    print(f'A maior nota de história foi de {maior_nota_aluno_his}: {maior_his} e a menor {menor_nota_aluno_his}: {menor_his}', file=arquivo)
