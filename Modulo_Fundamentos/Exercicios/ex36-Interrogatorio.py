''' Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" 

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" 
    e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
'''

print('=-'*17)
print ('| I N T E R R O G A T O R I O !! |')
print('=-'*17)
print('RESPONDA SOMENTE COM [S] ou [N]!')
      
while True:
    
    contagem = 0
    p1 = str(input('Telefonou para a vitima? [S]/[N]: ')).strip().upper()
    if p1 != 'S' and p1 != 'N':
        print('ENTRADA INVALIDA!')

    elif p1 == 'S':
        contagem += 1

    p2 = str(input('Esteve no local do crime? [S]/[N]: ')).strip().upper()
    if p2 != 'S' and p2 != 'N':
        print('ENTRADA INVALIDA!')

    elif p2 == 'S':
        contagem += 1

    p3 = str(input('Mora perto da vitima? [S]/[N]: ')).strip().upper()
    if p3 != 'S' and p3 != 'N':
        print('ENTRADA INVALIDA!')

    elif p3 == 'S':
        contagem += 1

    p4 = str(input('Devia para a vitima? [S]/[N]: ')).strip().upper()
    if p4 != 'S' and p4 != 'N':
        print('ENTRADA INVALIDA!')

    elif p4 == 'S':
        contagem += 1

    p5 = str(input('Ja trabalhou com a vitima? [S]/[N]: ')).strip().upper()
    if p5 != 'S' and p5 != 'N':
        print('ENTRADA INVALIDA!')
        break

    elif p5 == 'S':
        contagem += 1

    if contagem == 2:
        print('Pessoa Suspeita!')

    elif contagem == 3 or contagem == 4:
        print('Cúmplice!')

    elif contagem == 5:
        print('ASSASSINO!!!')

    else:
        print('INOCENTE!!!')

    dnv = input('Simular novamente? [S/N]: ').strip().upper()

    if dnv == 'S':
        continue
    elif dnv == 'N':
        print('Finalizando o Sistema...')
        break
    else:
        print('Entrada inválida! Digite apenas S ou N.')
