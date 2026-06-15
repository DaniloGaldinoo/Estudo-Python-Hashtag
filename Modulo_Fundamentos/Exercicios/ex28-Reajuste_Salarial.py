"""As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores
    e lhe contraram para desenvolver o programa que calculará os reajustes. 
    Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
*salários até R$ 280,00: aumento de 20% 
*salários entre R$ 280,00 e R$ 700,00 : aumento de 15% 
*salários entre R$ 700,00 e R$ 1500,00 : aumento de 10% 
*salários de R$ 1500,00 em diante : aumento de 5% 
Após o aumento ser realizado, informe na tela: 
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento."""

while True:

    print('=-'*9)
    print('| T A B A J A R A |')
    print('=-'*9)

    sal = float(input('Informe o Salario R$: '))

    if sal <= 280:
        bonus = sal * 0.20

        print(f'O salario antes do reajuste, era R$: {sal:.2f}')
        print(f'O aumento foi de 20%, que corresponde a R$: {bonus:.2f}')
        print(f'Sendo assim o novo salario é de R$: {sal + bonus:.2f}')

    elif sal > 280 and sal <= 700:
        bonus = sal * 0.15

        print(f'O salario antes do reajuste, era R$: {sal:.2f}')
        print(f'O aumento foi de 15%, que corresponde a R$: {bonus:.2f}')
        print(f'Sendo assim o novo salario é de R$: {sal + bonus:.2f}')

    elif sal > 700 and sal <= 1500:
        bonus = sal * 0.10

        print(f'O salario antes do reajuste, era R$: {sal:.2f}')
        print(f'O aumento foi de 10%, que corresponde a R$: {bonus:.2f}')
        print(f'Sendo assim o novo salario é de R$: {sal + bonus:.2f}')
    
    else:
        bonus = sal * 0.05

        print(f'O salario antes do reajuste, era R$: {sal:.2f}')
        print(f'O aumento foi de 5%, que corresponde a R$: {bonus:.2f}')
        print(f'Sendo assim o novo salario é de R$: {sal + bonus:.2f}')

    cont = input('Deseja calcular novamente? [S/N]: ').strip().upper()

    if cont == 'S':
        continue
    elif cont == 'N':
        print('Finalizando o Sistema...')
        break
    else:
        print('Entrada inválida! Digite apenas S ou N.')