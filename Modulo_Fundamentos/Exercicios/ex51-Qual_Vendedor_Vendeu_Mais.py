''' Crie um programa que consiga descobrir qual dos vendedores vendeu mais
# As vendas dos vendedores são listas com a quantidade vendida por cada vendedor
'''

vendas = [
    [10, 20, 100, 80, 90, 100, 20, 30, 44, 55, 33, 34, 100, 90, 80, 39, 87, 45, 50, 50, 50, 50, 40, 30, 3, 93, 39, 49, 88],    
    [100, 1, 1, 4, 5, 90, 100, 20, 4, 5, 100, 100, 100, 100, 100, 93, 20, 15, 40, 90, 90, 90, 90, 90, 90, 33, 22, 44, 43, 34],
]
vendedor1 = sum(vendas[0])
vendedor2 = sum(vendas[1])

if vendedor1 > vendedor2:
    print(f'O vendedor 1 fez mais vendas; com um total de {vendedor1} vendas!')
elif vendedor2 > vendedor1:
    print(f'O vendedor 2 fez mais vendas; com um total de {vendedor2} vendas!')
else:
    print(f'Os dois vendedores empataram com {vendedor1} vendas!')
