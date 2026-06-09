# Faça um Programa que peça dois números e imprima o maior deles.

while True:
    
    n1 = int(input('Insira o 1º Numero: '))
    n2 = int(input('Insira o 2º Numero: '))

    if n1 > n2:
        print (f'O maior numero inserido foi: {n1}')
    else:
        print (f'O maior numero inserido foi: {n2}')

    loop = input(str('Quer jogar novamente? [S/N]')).upper()
    
    if loop not in ('S', 'N'):
        print('Valor invalido. Encerrando!')
        break
    elif loop == "N":
        print('Ok, Encerrando Programa. . .')
        break
    else:
        print('Vamos para mais uma partida então! =D')
        pass