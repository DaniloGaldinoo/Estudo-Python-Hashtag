# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
#   sabendo que a decisão é sempre pelo mais barato.

while True:

    prod1 = float(input('Insira o valor do 1º Produto: '))
    prod2 = float(input('Agora do 2º produto: '))
    prod3 = float(input('Agora do 3º produto: '))

    if prod1 < prod2 and prod1 < prod3:
        print(f'O produto mais barato é o PRIMEIRO, custando R$: {prod1}')
    elif prod2 < prod1 and prod2 < prod3:
        print(f'O produto mais barato é o SEGUNDO, custando R$: {prod2}')
    elif prod3 < prod1 and prod3 < prod2:
        print(f'O produto mais barato é o TERCEIRO, custando R$: {prod3}')
    elif prod1 == prod2 and prod1 < prod3:
        print(f'O PRIMEIRO e o SEGUNDO produto estão mais baratos, com o mesmo preço; custando R$: {prod1}')
    elif prod1 == prod3 and prod1 < prod2:
        print(f'O PRIMEIRO e o TERCEIRO produto estão mais baratos, com o mesmo preço; custando R$: {prod1}')
    elif prod2 == prod3 and prod2 < prod1:
        print(f'O SEGUNDO e o TERCEIRO produto estão mais baratos, com o mesmo preço; custando R$: {prod2}')
    else:
        print(f'Todos os preços são iguais! Custando R$: {prod1}')



    cont = input('Deseja calcular novamente? [S/N]: ').strip().upper()

    if cont == 'S':
        continue
    elif cont == 'N':
        print('Finalizando o Sistema...')
        exit()
    else:
        print('Entrada inválida! Digite apenas S ou N.')