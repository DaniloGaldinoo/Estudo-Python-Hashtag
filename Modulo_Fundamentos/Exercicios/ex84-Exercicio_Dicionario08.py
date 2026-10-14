''' - Uma empresa está analisando os resultados de vendas do 1º semestre de 2022 e 2023
    - Qual foi o % de crescimento de cada mês de 2023 em relação a 2022?
    - Depois de calcular isso, calcule o valor total de crescimento de 2023 em relação a 2022
'''

vendas_22 = {"jan": 15000, "fev": 15500, "mar": 14000, "abr": 16600, "mai": 16300, "jun": 17000}
vendas_23 = {"jan": 17000, "fev": 15000, "mar": 17500, "abr": 16900, "mai": 16000, "jun": 18500}

# Calculando o total de vendas de cada semestre
total_22 = sum(vendas_22.values())
total_23 = sum(vendas_23.values())

# Calculando o crescimento total do semestre
totcresc = (total_23 / total_22) - 1

# Calculando o crescimento mensal
for mes in vendas_22:
    venda22 = vendas_22[mes]
    venda23 = vendas_23[mes]

    crescimento = (venda23 / venda22) - 1

    print(f'O crescimento em {mes} foi de: {crescimento:.2%}')

print(f'O crescimento total do semestre foi de: {totcresc:.2%}')