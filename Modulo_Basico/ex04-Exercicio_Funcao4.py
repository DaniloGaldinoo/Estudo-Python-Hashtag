''' Cálculo do Percentual e da Lista de Vendedores

- Queremos criar uma function que consiga identificar os vendedores que bateram uma meta, mas além disso, 
    consigo já me dar como resposta o cálculo do % da lista de vendedores que bateu a meta (para eu não precisar calcular manualmente depois)
- Essa function deve receber 2 informações como parâmetro: a meta e um dicionário com os vendedores e suas vendas. 
    E me dar 2 respostas: uma lista com o nome dos vendedores que bateram a meta e o % de vendedores que bateu a meta.
'''

meta = 10000
vendas = {
    'João': 15000,
    'Julia': 27000,
    'Marcus': 9900,
    'Maria': 3750,
    'Ana': 10300,
    'Alon': 7870,
}

def bateram_meta(vendedores, meta):
    meta_batida = []
    qtd_vendedores = len(vendedores)

    for nome, venda in vendedores.items(): #Usei o .items para fazer o unpacking do dicionario. Facilita muito na hora de usar as informações.
        
        if venda >= meta:
            meta_batida.append(nome)

    percent_meta = len(meta_batida) / qtd_vendedores


    return(meta_batida, percent_meta)


lista_vendedores, percentual = bateram_meta(vendas, meta) #Aqui eu fiz o unpacking do RETURN, dando variaveis independentes para cada retorno... Para nao precisar usar indices (valores_retorno[0])

print('Os vendedores que bateram a meta foram:\n')

for nome in lista_vendedores: 
    print(nome)

print(f'\nO percentual de vendedores que bateu a meta foi de {percentual:.2%}')