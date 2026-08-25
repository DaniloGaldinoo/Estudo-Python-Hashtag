''' Faça um programa que peça para o usuário inserir o faturamento dos últimos 5 meses (individualmente) 
e informe o maior faturamento
'''
c = 1
maior = 0

while c <= 5:
    fat = int(input(f'Informe o faturamento do {c}º mes: '))

    if fat > maior:
        maior = fat
        mes = c

    c += 1

print(f'O maior faturamento foi no mes de {mes}, com um total de {maior}')