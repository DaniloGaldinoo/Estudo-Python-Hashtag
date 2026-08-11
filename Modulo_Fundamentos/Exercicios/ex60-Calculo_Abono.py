''' As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom resultado alcançado durante o ano que passou.
Para isto contratou você para desenvolver a aplicação que servirá como uma projeção de quanto será gasto com o pagamento deste abono.
Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes do sindicato laboral, 
    chegou-se a seguinte forma de cálculo:

. Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro;
. O piso do abono será de 100 reais, isto é, aqueles funcionários cujo salário for muito baixo, recebem este valor mínimo; 

Neste momento, não se deve ter nenhuma preocupação com colaboradores com tempo menor de casa, descontos, impostos ou outras particularidades. 
O programa deverá calcular o valor do abono concedido a cada colaborador, de acordo com a regra definida acima. 

Ao final, o programa deverá apresentar:

O salário de cada funcionário, juntamente com o valor do abono;
O número total de funcionário processados;
O valor total a ser gasto com o pagamento do abono;
O número de funcionário que receberá o valor mínimo de 100 reais;
O maior valor pago como abono; 

A tela abaixo é um exemplo de execução do programa, apenas para fins ilustrativos.

Projeção de Gastos com Abono
============================ 
 
Salário: 1000
Salário: 300
Salário: 500
Salário: 100
Salário: 4500
Salário: 0
 
Salário    - Abono     
R$ 1000.00 - R$  200.00
R$  300.00 - R$  100.00
R$  500.00 - R$  100.00
R$  100.00 - R$  100.00
R$ 4500.00 - R$  900.00
 
Foram processados 5 colaboradores
Total gasto com abonos: R$ 1400.00
Valor mínimo pago a 3 colaboradores
Maior valor de abono pago: R$ 900.00
'''

lista_salarios = [1000, 300, 500, 200, 1500, 3000, 3400, 5000, 7000, 2000, 600, 800, 250, 1500, 20000]
abonos = []
total_colab = 0
minimo = 0
maior = 0

print('Projeção de Gastos com Abono')
print('='*28)

for salarios in lista_salarios:
    print (f'Salário: {salarios}')
    total_colab += 1

print('\n\nSalário   |   Abono')

for i, sal in enumerate(lista_salarios):
    abono = sal * 0.2

    if abono <= 100:
        abono = 100
        minimo += 1

    if abono > maior:
        maior = abono

    abonos.append(abono)

    print(f'R$ {sal:.2f}   -  R$ {abono:.2f}')

tot_abono = sum(abonos) 
print(f'\n\nForam processados {total_colab} colaboradores')
print(f'Total gasto com abonos: R$ {tot_abono:.2f}') 
print(f'Valor minimo pago a {minimo} colaboradores')
print(f'Maior Valor de abono pago: R$ {maior:.2f}')