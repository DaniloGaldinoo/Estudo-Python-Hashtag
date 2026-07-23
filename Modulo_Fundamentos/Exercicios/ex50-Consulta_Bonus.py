''' Crie um sistema de consulta de bônus dos funcionários
# Seu sistema deve:
# - Pegar o valor de vendas do funcinoário por meio de um input
# - Calcular o bônus do funcionário de acordo com a seguinte regra:
#       - Se o funcionário vendeu mais de 1000 unidades, ele ganha R$2 de bonus para cada unidade vendida
#       - Se o funcionário vendeu mais de 5000 unidades, ele ganha R$2 de bônus para cada unidade + um valor fixo de R$1000
#       - Se o funcionário vendeu menos de 1000 unidades, ele não ganha bônus
# - Printar no final o valor do bônus do funcionário
'''

vendas = int(input('Insira a quantidade de vendas do funcionario: '))

if vendas <= 1000:
    print('Que pena. Dessa vez nao vai ter bonus. . .')
elif vendas > 1000 and vendas <=5000:
    bonus = vendas * 2
    print(f'O total do bonus deste funcionario foi de R$: {bonus:.2f}')
else:
    bonus = vendas * 2
    print(f'O total do bonus deste funcionario foi de R$: {1000 + bonus:.2f}')