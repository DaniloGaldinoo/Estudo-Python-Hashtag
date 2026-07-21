''' Faturamento do Melhor e do Pior Mês do Ano
Qual foi o melhor mês do Ano e quanto vendeu?
E valor do pior mes de vendas e mês do ano?

Calcule tambem o faturamento total do ano e quanto que o melhor mes representou do faturamento total.
'''


meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]

vendas_1sem.extend(vendas_2sem)
maior = max(vendas_1sem)
menor = min(vendas_1sem)
locmaior = vendas_1sem.index(maior)
locmenor = vendas_1sem.index(menor)
total = sum(vendas_1sem)
percent = maior / total


print(f'O mes que mais vendeu foi {meses[locmaior]}, com um total de vendas de R$: {maior:,.2f}\nE o mes que menos vendeu foi {meses[locmenor]}, com um total de vendas de R$: {menor:,.2f}')
print(f'O faturamento total do ano foi de R$: {total:,.2f}')
print(f'O melhor mes representou {percent:.1%} das vendas do ano todo.')


''' Crie uma lista com o top 3 valores de vendas do ano.'''

top3 = []

for i in range (0,3):
    maior = max(vendas_1sem)
    top3.append(maior)
    vendas_1sem.remove(maior)

print(top3)