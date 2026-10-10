''' Agora edite o programa anterior para fazer com que, caso não exista o produto, 
    o programa pergunte se o usuário quer cadastrar o produto
Se ele responder sim, o programa deve pedir o nome do produto e o preco do produto e cadastrar no dicionário de preços
Em seguida do cadastro bem sucedido, o programa deve printar o dicionário de precos atualizado
'''

precos = {"celular": 1500, "camera": 1000, "fone de ouvido": 800, "monitor": 2000}

while True:
    prod = input('Insira o nome do produto: ').lower().strip()

    if prod in precos:
        print(f'O valor de {prod} é R$: {precos[prod]}')
        break
    else:
        print('Produto não encontrado.')
        resp = input('Deseja cadastrar um novo produto? [S/N]').strip().upper()
        if resp == 'S':
            print('*-'*10)
            print('CADASTRO DE PRODUTOS')

            nome = input('Insira o nome do produto: ').lower().strip()
            valor = float(input('Insira o valor do produto R$: '))

            precos[nome] = valor   #No dicionário precos, associe a chave nome ao valor valor

            print(f'Dicionario atualizado: {precos}')
            break
        else:
            print('Consultando novamente!')
            continue

