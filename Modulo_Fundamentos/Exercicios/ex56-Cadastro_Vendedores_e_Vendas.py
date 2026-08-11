''' Faça um Programa que leia as vendas dos vendedores, mostre a venda de cada vendedor com o seu nome e a média de vendas. 
'''

vendas = [1000, 1500, 1200, 1300]
vendedores = ["Fulano", "Beltrano", "Ciclano", "Lira"]

for i, venda in enumerate(vendas):
    print(f'O vendedor {vendedores[i]}, vendeu {vendas}')