''' Calculando % de uma lista

Faremos algo parecido com "filtrar" uma lista. 
Mais pra frente no curso aprenderemos outras formas de fazer isso, mas com o nosso conhecimentoa atual já conseguimos resolver o desafio

Digamos que a gente tenha uma lista de vendedores e ao invés de saber todos os vendedores que bateram a meta, 
eu quero conseguir calcular o % de vendedores que bateram a meta. 
Ou seja, se temos 10 vendedores e 3 bateram a meta, temos 30% dos vendedores que bateram a meta. 
E para treinar uma estrutura parecida, informe quem foi o vendedor que mais vendeu.

'''


meta = 10000
meta_batida = []
melhor_vendedor = ''
maior_venda = 0
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
]

for i in vendas:
    if i[1] >= meta:
        meta_batida.append(i)
    if i[1] > maior_venda:
        maior_venda = i[1]
        melhor_vendedor = i[0]    

print(f'Apos verificação das metas, concluimos que {len(meta_batida) / len(vendas):.2%} dos vendedores conseguiram bater a meta!')
print(f'O vendedor que mais vendeu foi: [ {melhor_vendedor} ]! Com um total de {maior_venda} em vendas.')