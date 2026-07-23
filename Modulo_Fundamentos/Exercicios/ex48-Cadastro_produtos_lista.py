'''Crie um sistema de cadastro de produtos em uma lista de produtos
# Seu sistema deve:
# - Pegar o usuário qual produto vai ser cadastrado por meio de um input
# - Garantir que se o usuário escrever com letra maiúscula ou minúscula, o produto continua sendo o mesmo produto
# - Se o usuário inserir um produto que já existe na lista, o programa deve printar a mensagem "Produto já existente, tente novamente"
# - Se o usuário inserir um produto que não existe na lista, o programa deve inserir na lista, printar a mensagem 
        Produto X cadastrado com sucesso e em seguida printar a lista completa
'''

produtos = ["celular", "camera", "fone de ouvido", "monitor"]

while True:
    prod = input('Insira o nome do produto: ').lower().strip()
    if prod in produtos:
        print('Produto já existente, tente novamente!')
    
    else:
        produtos.append(prod)
        print(f'Produto {prod} adicionado com sucesso!')
        print(produtos)

    resp = input('Deseja adicionar mais produtos? [S/N]').lower().strip()
    if resp != 'n' and resp != 's':
        print('Entrada Invalida.\n Sistema Encerrado!')
        break
    
    elif resp == 'n':
        print('Encerrando . . .')
        break
    else:
        continue