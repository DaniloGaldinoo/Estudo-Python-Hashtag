# Faça um programa que leia o orçamento de 3 empresas e mostre o maior deles.

while True:

    empresa1 = float (input('Informe o orçamento da 1ª empresa: '))
    empresa2 = float (input('Agora informe da 2ª: '))
    empresa3 = float (input('Informe agora da 3ª: '))
    maior = empresa1

    if empresa1 >= empresa2 and empresa1 >= empresa3:
        print(f'O maior orçamento declarado foi da 1ª empresa! Com um valor de {maior}')
    
    elif empresa2 >= empresa1 and empresa2 >= empresa3:
        maior = empresa2
        print(f'O maior orçamento declarado foi da 2ª empresa! Com um valor de {maior}')
    
    else:
        maior = empresa3
        print(f'O maior orçamento declarado foi da 3ª empresa! Com um valor de {maior}')

    cont = str(input('Deseja Calcular Novamente? [S/N] :')).strip().upper()

    if cont == "S":
        continue
    elif cont =="N":
        print ('Finalizando o Sistema. . .')
        break
    else:
        print('Entrada Invalida!')