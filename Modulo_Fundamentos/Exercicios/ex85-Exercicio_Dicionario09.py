''' - No final da reunião de apresentação dos números, seu chefe perguntou:
    - E se nos meses de 2023 que a gente vendeu menos do que 2022 a gente tivesse pelo menos empatado com 2022 
        (ou seja, se nos meses de 2023 em que as vendas foram menores do que o mesmo mês em 2022, o valor de vendas tivesse sido igual a 2022)
    - Qual teria sido o nosso crescimento de 2023 frente a 2022?
'''

vendas_22 = {"jan": 15000, "fev": 15500, "mar": 14000, "abr": 16600, "mai": 16300, "jun": 17000}
vendas_23 = {"jan": 17000, "fev": 15000, "mar": 17500, "abr": 16900, "mai": 16000, "jun": 18500}

total_22 = sum(vendas_22.values())
total_23_ajustado = 0

for mes in vendas_22:
    venda22 = vendas_22[mes]
    venda23 = vendas_23[mes]

    if venda23 < venda22:
        venda23 = venda22

    total_23_ajustado += venda23

crescimento = (total_23_ajustado / total_22 - 1) * 100

print(f"Total de vendas em 2022: R$ {total_22:,.2f}")
print(f"Total ajustado de vendas em 2023: R$ {total_23_ajustado:,.2f}")
print(f"Crescimento hipotético: {crescimento:.2f}%")
