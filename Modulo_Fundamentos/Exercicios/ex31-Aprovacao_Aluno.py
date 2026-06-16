'''
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média.
Em seguida, mostre qual conceito o aluno teve.

Média de Aproveitamento  Conceito
Entre 9.0 e 10.0            A
Entre 7.5 e 9.0             B
Entre 6.0 e 7.5             C
Entre 4.0 e 6.0             D
Entre 4.0 e zero            E
'''

nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota: '))

media = (nota1 + nota2) / 2

if nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10:
    print('Alguma das notas foi inserida de forma inválida!')

elif media >= 9 and media <= 10:
    print('CONCEITO = [A]')

elif media >= 7.5 and media < 9:
    print('CONCEITO = [B]')

elif media >= 6 and media < 7.5:
    print('CONCEITO = [C]')

elif media >= 4 and media < 6:
    print('CONCEITO = [D]')

else:
    print('CONCEITO = [E]')