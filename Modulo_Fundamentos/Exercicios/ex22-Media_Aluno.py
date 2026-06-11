# Faça um programa para leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# Aprovado para maior ou igual a sete/ Reprovado para menor que sete/ Aprovado com Distinção se for 10.

while True:

    nota1 = float(input('Insira a 1ª nota: '))
    nota2 = float(input('Insira a 2ª nota: '))
    media = (nota1 + nota2)/2

    print (f'A media foi de: {media:.1f}')

    if media == 10:
        print ('Aprovado com distinção!')
    elif media >= 7:
        print ('Aprovado!')
    else:
        print ('Reprovado!')

    con = str(input('Deseja calcular novamente? [S/N] : ')).upper()
    
    if con == 'S':
        continue
    else:
        print ('Finalizando sistema. . .')
        break
