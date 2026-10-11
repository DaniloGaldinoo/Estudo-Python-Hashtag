''' - Edite o programa antigo para ter os 2 dicionários, o de preços originais e o de novos preços
 - Em seguida calcule o valor total de reajuste em R$ que teve entre a lista de produtos original e a lista final
'''

precos = {"celular": 1500, "camera": 1000, "fone de ouvido": 800, "monitor": 3000}

precos_originais = precos.copy()
total_reaj = 0

for produto in precos:
    novovalor = 0 
    if precos[produto] <= 1000:
        reajuste = precos[produto] * 0.10
        novovalor = precos[produto] + reajuste
        precos[produto] = novovalor
        total_reaj += reajuste
    elif precos[produto] > 1000 and precos[produto] <= 2000:
        reajuste = precos[produto] * 0.15
        novovalor = precos[produto] + reajuste
        precos[produto] = novovalor
        total_reaj += reajuste
    else:
        reajuste = precos[produto] * 0.20
        novovalor = precos[produto] + reajuste
        precos[produto] = novovalor
        total_reaj += reajuste

precos_novos = precos.values()

print(f'Os valores originais são: {precos_originais}')
print(f'Os novos valores são: {precos_novos}')
print(f'A diferença em reais entre eles é de R$: {total_reaj:,.2f}')


'''

precos = {"celular": 1500, "camera": 1000, "fone de ouvido": 800, "monitor": 3000}
novos_precos = {}
for produto in precos:
    preco_produto = precos[produto]
    if preco_produto <= 1000:
        novo_preco = preco_produto * 1.1
    elif preco_produto <= 2000:
        novo_preco = preco_produto * 1.15
    else:
        novo_preco = preco_produto * 1.2
    print(f"Produto {produto}, Novo Preço: R${novo_preco}")
    novos_precos[produto] = novo_preco
total_antigo = sum(precos.values())
total_novo = sum(novos_precos.values())
reajuste = total_novo - total_antigo
print(f"O reajuste total foi de R${reajuste}")

'''