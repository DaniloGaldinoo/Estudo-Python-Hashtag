''' Uma fruteira está vendendo frutas com a seguinte tabela de preços:

                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. 
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e 
escreva o valor a ser pago pelo cliente.
'''

morango = float(input('Insira a quantidade de quilos de MORANGOS comprados: '))
maca = float(input('Insira a quantidade de quilos de MAÇÃ comprados: '))
totkg = morango + maca

if morango <= 5:
    vlrmorango = 2.50
else:
    vlrmorango = 2.20

if maca <= 5:
    vlrmaca = 1.80
else:
    vlrmaca = 1.50

totmorango = morango * vlrmorango
totmaca = maca * vlrmaca
vlrtotal = totmorango + totmaca

if totkg > 8 or vlrtotal > 25:
    desc = vlrtotal * 0.10
    totcomdesc = vlrtotal - desc
    print(f'A maçã deu um total de R$:{totmaca}')
    print(f'O morango deu um total de R$:{totmorango}')
    print(f'O valor a ser pago é de R$: {totcomdesc}, com uma quantidade total de {totkg}')
else:
    print(f'A maçã deu um total de R$:{totmaca}')
    print(f'O morango deu um total de R$:{totmorango}')
    print(f'O valor a ser pago é de R$: {vlrtotal}, com uma quantidade total de {totkg}')