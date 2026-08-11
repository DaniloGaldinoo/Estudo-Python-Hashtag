''' Faça um Programa que crie uma lista com as médias de cada aluno, 
        imprima as médias de cada aluno e a quantidade de alunos com média maior que 7.
'''

alunos = ["José", "Joana", "Maria", "Carla", "Mauricio", "Andre", "Tiago", "Enzo", "Amanda", "Alessandra"]
media_positiva = 0
notas = [
    [10, 9, 8, 8],
    [9, 7, 6, 4],
    [10, 10, 10, 10],
    [5, 3, 10, 9],
    [7, 6, 6, 6],
    [7, 7, 8, 7],
    [7, 7, 7, 9],
    [8, 5, 6, 7],
    [10, 9, 7, 4],
    [10, 1, 3, 3],
]

for i, aluno in enumerate(alunos):
    media = (notas[i][0] + notas[i][1] + notas[i][2] + notas[i][3]) / 4
    print(f'[{aluno}] Media: {media:.2f}')

    if media > 7:
        media_positiva += 1
print(f'Contabilizando todos os alunos, obtivemos um total de {media_positiva} notas acima de 7!')