''' Faça um Programa para um caixa eletrônico. 
    O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. 
    As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. 
    O valor mínimo é de 10 reais e o máximo de 600 reais. 
    O programa não deve se preocupar com a quantidade de notas existentes na máquina.
'''

print('-'*22)
print('|  CAIXA ELETRONICO  |')
print('-'*22)
total = int(input('Informe o valor que deseja sacar (Entre 10 e 600 reais). R$:'))

um = 0
cinco = 0
dez = 0
cinquenta = 0
cem = 0

if total < 10 or total > 600:
    print('Valor Invalido!')
else:
    while total >= 100:
        total = total - 100
        cem += 1

    while total >= 50:
        total = total - 50
        cinquenta += 1

    while total >= 10:
        total = total - 10
        dez += 1

    while total >= 5:
        total = total - 5
        cinco += 1

    while total >= 1:
        total = total - 1
        um += 1

    print('S A C A N D O . . .')
    print(f'Notas sacadas:\n[{cem}] - R$:100,00\n[{cinquenta}] - R$:50,00\n[{dez}] - R$:10,00\n[{cinco}] - R$:5,00\n[{um}] - R$:1,00')