''' Um posto está vendendo combustíveis com a seguinte tabela de descontos:

Álcool: até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro

Gasolina:até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro

Escreva um algoritmo que leia o número de litros vendidos, 
o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), 
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 
o preço do litro do álcool é R$ 1,90.
'''

alc = 1.90
gasol = 2.50

litros = float(input('Insira a quantidade de litros: '))
tipo_comb = input('Selecione o tipo de combustivel!\n[A] - Alcool\n[G] - Gasolina\nInsira [A] ou [G]: ').strip().upper()

if tipo_comb != 'A' and tipo_comb != 'G':
    print('Entrada Invalida.')

elif tipo_comb == 'A':
    total = litros * alc

    if litros <= 20:
        desc = total * 0.03
    else:
        desc = total * 0.05

    print(f'O valor a ser pago é de R$: {total - desc:.2f}')

else:
    total = litros * gasol

    if litros <= 20:
        desc = total * 0.04
    else:
        desc = total * 0.06

    print(f'O valor a ser pago é de R$: {total - desc:.2f}')