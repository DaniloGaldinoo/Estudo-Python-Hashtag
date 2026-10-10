''' Crie um sistema de consulta de preços
        Seu sistema deve:

- Pedir para o usuário o nome de um produto
- Caso o produto exista na lista de produtos, o programa deve retornar o preço do produto como resposta
       - Ex: O produto celular custa R$1500
- Caso o produto não exista na lista de produtos, o programa deve printar uma mensagem para o usuário tentar novamente
'''

precos = {"celular": 1500, "camera": 1000, "fone de ouvido": 800, "monitor": 2000}

while True:
    prod = input('Insira o nome do produto: ').lower().strip()

    if prod in precos:
        print(f'O valor de {prod} é {precos[prod]}')
        break
    else:
        print('Produto não encontrado. Tente novamente!')
        continue