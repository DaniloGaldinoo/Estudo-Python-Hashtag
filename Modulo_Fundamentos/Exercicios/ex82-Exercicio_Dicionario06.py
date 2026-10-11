''' Dada a lista de preços de produtos, uma loja resolveu fazer um reajuste nos preços dos produtos. 
calcule o novo valor dos produtos com base nas seguintes regras:
- Preços até 1.000 vão ter um reajuste de 10% (ou seja, o novo preço será 110% do preço atual)
- Preços até maiores que 1.000 até 2.000 vão ter reajuste de 15%
- Preços acima de 2.000 vão ter reajuste de 20%
'''

precos = {"celular": 1500, "camera": 1000, "fone de ouvido": 800, "monitor": 3000}


for produto in precos:
    novovalor = 0 
    if precos[produto] <= 1000:
        reajuste = precos[produto] * 0.10
        novovalor = precos[produto] + reajuste
        precos[produto] = novovalor
    elif precos[produto] > 1000 and precos[produto] <= 2000:
        reajuste = precos[produto] * 0.15
        novovalor = precos[produto] + reajuste
        precos[produto] = novovalor
    else:
        reajuste = precos[produto] * 0.20
        novovalor = precos[produto] + reajuste
        precos[produto] = novovalor

print (precos)