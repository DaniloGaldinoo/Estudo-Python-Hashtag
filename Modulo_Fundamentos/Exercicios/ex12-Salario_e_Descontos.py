# Calculadora de Salário e Descontos
hrsal = float(input('Digite o valor da sua hora de trabalho: '))
hrtrab = float(input('Digite o número de horas trabalhadas no mês: '))

salbruto = hrsal * hrtrab
ir = salbruto * 0.11
inss = salbruto * 0.08
sindicato = salbruto * 0.05
salliquido = salbruto - ir - inss - sindicato

print(f'Salário Bruto: R$ {salbruto:.2f}')
print(f'IR (11%): R$ {ir:.2f}') 
print(f'INSS (8%): R$ {inss:.2f}')
print(f'Sindicato (5%): R$ {sindicato:.2f}')
print(f'Salário Líquido: R$ {salliquido:.2f}')  
