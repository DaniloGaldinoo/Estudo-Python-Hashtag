''' O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
    porém não há limites para a quantidade de carne por cliente. 
Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. 
Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, 
contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
'''

tipo = int(input('Informe qual o tipo de carne o cliente esta comprando: \n[1] - File Duplo\n[2] - Alcatra\n[3] - Picanha\nInsira o numero correspondente: '))
kg = float(input('Informe a quantidade (KG): '))
desc = 0.05

if tipo == 1 and kg <= 5:
    file = 4.90
    total = file * kg
    carne = 'File Duplo'
elif tipo == 1 and kg > 5:
    file = 5.80
    total = file * kg
    carne = 'File Duplo'

elif tipo == 2 and kg <= 5:
    alcatra = 5.90
    total = alcatra * kg
    carne = 'Alcatra'
elif tipo == 2 and kg > 5:
    alcatra = 6.80
    total = alcatra * kg
    carne = 'Alcatra'

elif tipo == 3 and kg <= 5:
    picanha = 6.90
    total = picanha * kg
    carne = 'Picanha'
elif tipo == 3 and kg > 5:
    picanha = 7.80
    total = picanha * kg
    carne = 'Picanha'
else:
    print('Tipo de carne inválido!')
    exit()

conv = int(input('Informe o metodo de pagamento!\n[1] - Cartão Tabajara\n[2] - Dinheiro\n[3] - Cartão Débito\n[4] - Cartão de Crédito'))
if conv == 1:
    pagamento = 'Cartão Tabajara'
elif conv == 2:
    pagamento = 'Dinheiro'
elif conv == 3:
    pagamento = 'Cartão Débito'
elif conv == 4:
    pagamento = 'Cartão Crédito'

if conv == 1:
    desctot = total * desc
    novotot = total - desctot

    print('CUPOM FISCAL')
    print(f'Pagamento via {pagamento}!')
    print(f'{carne}   x   {kg}KG   | R$:{total}')
    print(f'Desconto de 5% aplicado: R$:{desctot}')
    print(f'Valor pago!   R$:{novotot}')
    print('OBRIGADO E VOLTE SEMPRE!')
else:
    print('CUPOM FISCAL')
    print(f'Pagamento via {pagamento}!')
    print(f'{carne}   x   {kg}KG   | R$:{total}')
    print(f'Valor pago!   R$:{total}')
    print('OBRIGADO E VOLTE SEMPRE!')