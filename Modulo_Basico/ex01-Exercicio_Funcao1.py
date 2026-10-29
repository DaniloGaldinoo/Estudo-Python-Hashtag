'''
Function para Cálculo de Carga Tributária
(Lembrando, não se atente ao funcionamento real da carga tributária, é apenas um exemplo imaginário para treinarmos as functions com algo mais prático)

Imagine que você trabalha no setor contábil de uma grande empresa de Varejo. 
    Crie uma function que calcule qual o % de carga tributária que está sendo aplicado sobre um determinado produto, 
dado o preço de venda, o "lucro" e os custos (com exceção do imposto) dele.

Repare que preço - custo não é igual ao lucro, porque ainda foi descontado o imposto. 
Sua functiona deve calcular qual foi o % de imposto aplicado sobre o preço total.

'''

preco = 1500
custo = 400
lucro = 800

def calculo_carga_trib (preco_venda, custo_produto, lucro_desejado):
    imposto = preco_venda - custo_produto - lucro_desejado
    calc = imposto / preco_venda

    return calc

carga = calculo_carga_trib(preco, custo, lucro)

print (f'O imposto aplicado foi de {carga:.2%}')
