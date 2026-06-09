# Crie um sistema para ser usado pelo time de controle de estoque de um centro de distribuição.
# Imagine que ao fim do todo dia, o time conta quantas unidades de produto existem no . Se tivermos um estoque abaixo do estoque permitido
#   para aquela categoria de produto, o time deve ser avisado para fazer um novo pedido daquele produto.
# Cada categoria de produto tem um estoque minimo diferente, segundo a regra abaixo:
# Alimentos -> Minimo de 50 | Bebidas -> Minimo de 75 | Limpeza -> Minimo de 30

print('-=' * 20)
print('| C O N T R O L E  D E  E S T O Q U E !|')
print('-=' * 20)

while True:
    nomeprod = input('Insira o nome do produto: ')
    catprod = int(input('Categorias:\n[1] Alimentos\n[2] Bebidas\n[3] Limpeza\nDigite qual a categoria do produto: '))

    if catprod not in (1, 2, 3):
        print('Categoria inválida!')
        break

    qtdprod = int(input('Qual a quantidade atual em estoque? '))

    if catprod == 1:
        minimo = 50
        categoria = 'Alimentos'
    elif catprod == 2:
        minimo = 75
        categoria = 'Bebidas'
    else:
        minimo = 30
        categoria = 'Limpeza'

    if qtdprod < minimo:
        print(f'\nO item {nomeprod} está abaixo do estoque mínimo!')
        print(f'Categoria: {categoria}')
        print(f'Estoque mínimo: {minimo}')
        print(f'Estoque atual: {qtdprod}')
        print('Por favor, faça um pedido de reposição!')
    else:
        print(f'\nQuantidade OK. Estoque atual: {qtdprod}')