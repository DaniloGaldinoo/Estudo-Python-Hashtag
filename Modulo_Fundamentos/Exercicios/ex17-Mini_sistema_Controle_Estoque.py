# Crie um sistema para ser usado pelo time de controle de estoque de um centro de distribuição.
# Imagine que ao fim do todo dia, o time conta quantas unidades de produto existem no estoque abaixo do estoque permitido.
#   para aquela categoria de produto, o time deve ser avisado para fazer um novo pedido daquele produto.
# Cada categproa de produto tem um estoque minimo diferente, segundo a regra abaixo:
# Alimentos -> Minimo de 50 | Bebidas -> Minimo de 75 | Limpeza -> Minimo de 30

while True:
    nomeprod = str(input('Insira o nome do produto: '))
    catprod = int(input('Categorias: \n[1] Alimentos\n[2] Bebidas\n[3] Limpeza\nDigite qual a categoria do produto: '))
    qtdprod = int(input('Qual a quantidade atual em estoque?'))

    if qtdprod < 50 and catprod = 1:
        print()