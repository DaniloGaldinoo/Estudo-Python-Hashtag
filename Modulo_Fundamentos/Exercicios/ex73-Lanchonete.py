''' O cardápio de uma lanchonete é o seguinte:

Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. 
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. 
Considere que o cliente deve informar quando o pedido deve ser encerrado.
'''

total = 0

while True:
    codigo = int(input('Insira o código do produto (0 para encerrar): '))

    if codigo == 0:
        break

    if codigo == 100:
        produto = 'Cachorro Quente'
        preco = 1.20

    elif codigo == 101:
        produto = 'Bauru Simples'
        preco = 1.30

    elif codigo == 102:
        produto = 'Bauru com Ovo'
        preco = 1.50

    elif codigo == 103:
        produto = 'Hambúrguer'
        preco = 1.20

    elif codigo == 104:
        produto = 'Cheeseburguer'
        preco = 1.30

    elif codigo == 105:
        produto = 'Refrigerante'
        preco = 1.00

    else:
        print('Código inválido! Tente novamente.')
        continue

    quantidade = int(input('Insira a quantidade: '))

    valor = preco * quantidade
    total += valor

    print(f'{produto} - {quantidade} unidade(s) - R$ {valor:.2f}')

print(f'\nTotal geral do pedido: R$ {total:.2f}')