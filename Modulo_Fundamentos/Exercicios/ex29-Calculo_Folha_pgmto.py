''' Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, 
    que depende do salário bruto (conforme tabela abaixo) e que o FGTS corresponde a 11% do Salário Bruto, 
    mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
    O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

Desconto do IR:
Salário Bruto até 900 - isento
Salário Bruto até 1500 - desconto de 5%
Salário Bruto até 2500 - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20%
Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

Salário Bruto: (5 * 220)        : R$ 1100,00
(-) IR (5%)                     : R$   55,00
(-) INSS ( 10%)                 : R$  110,00
FGTS (11%)                      : R$  121,00
Total de descontos              : R$  165,00
Salário Liquido                 : R$  935,00
'''


while True:

    print('=-'*20)
    print(f'{"CALCULO FOLHA DE PAGAMENTO":^40}')
    print('=-'*20)

    hr = float(input('| Insira o valor da hora trabalhada: '))
    qtdhr = float(input('| Insira a quantidade de horas trabalhadas: '))
    sal = hr * qtdhr
    if sal <= 900:
        ir = 0
        perc = '0%'
    elif sal > 900 and sal <= 1500:
        ir = 0.05
        perc = '5%'
    elif sal > 1500 and sal <= 2500:
        ir = 0.10
        perc = '10%'
    else:
        ir = 0.20
        perc = '20%'

    inss = sal*0.10
    valor_ir = sal * ir
    total_desc = valor_ir + inss
    sal_liquido = sal - valor_ir - inss
    fgts = sal * 0.11

    print(f'\n\nRELATORIO\n')
    print(f'Salario Bruto: ({hr}*{qtdhr}):    R$:{sal:.2f}')
    print(f'(-) IR ({perc}):        R$:{valor_ir:.2f}')
    print(f'(-) INSS (10%):        R$:{inss:.2f}')
    print(f'FGTS (11%):        R$:{fgts:.2f}')
    print(f'Total de descontos: R$:{total_desc:.2f}')
    print(f'Salario Liquido: R$: {sal_liquido:.2f}')

    cont = input('Deseja calcular novamente? [S/N]: ').strip().upper()

    if cont == 'S':
        continue
    elif cont == 'N':
        print('Finalizando o Sistema...')
        break
    else:
        print('Entrada inválida! Digite apenas S ou N.')