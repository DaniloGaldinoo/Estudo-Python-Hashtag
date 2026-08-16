''' Uma empresa paga seus vendedores com base em comissões. 
O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. 
Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, 
    ou seja, um total de $470. 
Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:

$200 - $299
$300 - $399
$400 - $499
$500 - $599
$600 - $699
$700 - $799
$800 - $899
$900 - $999
$1000 em diante

Existem várias formas de fazer. Faça primeiro da forma que parecer mais intuitiva para você.

Em seguida, caso queira um desafio:
Desafio: Crie uma forma para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.
'''

vendas = [1000, 2000, 3000, 4000, 5000, 6000, 5500, 4500, 3600]
bonus_semana = 200

contadores = [0] * 9

for venda in vendas:
    salario = bonus_semana + (venda * 0.09)

    if salario < 300:
        contadores[0] += 1

    elif salario < 400:
        contadores[1] += 1

    elif salario < 500:
        contadores[2] += 1

    elif salario < 600:
        contadores[3] += 1

    elif salario < 700:
        contadores[4] += 1

    elif salario < 800:
        contadores[5] += 1

    elif salario < 900:
        contadores[6] += 1

    elif salario < 1000:
        contadores[7] += 1

    else:
        contadores[8] += 1


print('Faixa salarial | Quantidade')
print(f'$200 - $299     | {contadores[0]}')
print(f'$300 - $399     | {contadores[1]}')
print(f'$400 - $499     | {contadores[2]}')
print(f'$500 - $599     | {contadores[3]}')
print(f'$600 - $699     | {contadores[4]}')
print(f'$700 - $799     | {contadores[5]}')
print(f'$800 - $899     | {contadores[6]}')
print(f'$900 - $999     | {contadores[7]}')
print(f'$1000 em diante | {contadores[8]}')