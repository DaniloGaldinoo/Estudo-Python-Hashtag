# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

num = int(input('Insira um valor: '))

if num > 0:
    print(f'O numero {num} é Positivo!')
elif num <0:
    print(f'O numero {num} é Negativo!')
else:
    print(f'O numero {num} é Nulo!')