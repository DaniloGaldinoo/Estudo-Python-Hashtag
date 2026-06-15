while True:

    n1 = float(input('Insira o valor do 1º numero: '))
    n2 = float(input('Agora o 2º: '))
    n3 = float(input('Agora o 3º: '))

    if n1 <= n2 and n1 <= n3:
        menor = n1
    elif n2 <= n1 and n2 <= n3:
        menor = n2
    else:
        menor = n3

    if n1 >= n2 and n1 >= n3:
        maior = n1
    elif n2 >= n1 and n2 >= n3:
        maior = n2
    else:
        maior = n3

    meio = n1 + n2 + n3 - maior - menor

    print(f'Os valores em ordem decrescente ficam: {maior}, {meio}, {menor}')

    cont = input('Deseja calcular novamente? [S/N]: ').strip().upper()

    if cont == 'S':
        continue
    elif cont == 'N':
        print('Finalizando o Sistema...')
        break
    else:
        print('Entrada inválida! Digite apenas S ou N.')