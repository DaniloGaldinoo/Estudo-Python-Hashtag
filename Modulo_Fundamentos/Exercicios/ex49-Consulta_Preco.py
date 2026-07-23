'''Crie um sistema de consulta de preços
# Seu sistema deve:
# - Pedir para o usuário o nome de um produto
# - Caso o produto exista na lista de produtos, o programa deve retornar o preço do produto como resposta
#        - Ex: O produto celular custa R$1500
# - Caso o produto não exista na lista de produtos, o programa deve printar uma mensagem para o usuário tentar novamente
'''

produtos = ["celular", "camera", "fone de ouvido", "monitor"]
precos = [1500, 1000, 800, 2000]

while True:
    prod = input('Insira o produto que deseja consultar o preço: ').lower().strip()

    if prod in produtos:
        i = produtos.index(prod)
        print(f'O produto {prod} custa R$:{precos[i]:.2f}')
        break
    else:
        print('Entrada Invalida. Tente novamente.')
        continue