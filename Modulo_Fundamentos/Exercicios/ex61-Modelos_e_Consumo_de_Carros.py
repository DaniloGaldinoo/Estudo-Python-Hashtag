''' Faça um programa que carregue uma lista com os modelos de cinco carros 
(exemplo de modelos: FUSCA, GOL, VECTRA etc). 
Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. 
Calcule e mostre:

* O modelo do carro mais econômico;
* Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros quanto isto custará, 
    considerando um que a gasolina custe R$ 2,25 o litro. 
    
Abaixo segue uma tela de exemplo. 
A disposição das informações deve ser o mais próxima possível ao exemplo. 
Os dados são fictícios

Comparativo de Consumo de Combustível

Veículo 1
Nome: fusca
Km por litro: 7
Veículo 2
Nome: gol
Km por litro: 10
Veículo 3
Nome: uno
Km por litro: 12.5
Veículo 4
Nome: Vectra
Km por litro: 9
Veículo 5
Nome: Peugeout
Km por litro: 14.5

Relatório Final
 1 - fusca           -    7.0 -  142.9 litros - R$ 321.43
 2 - gol             -   10.0 -  100.0 litros - R$ 225.00
 3 - uno             -   12.5 -   80.0 litros - R$ 180.00
 4 - vectra          -    9.0 -  111.1 litros - R$ 250.00
 5 - peugeout        -   14.5 -   69.0 litros - R$ 155.17
O menor consumo é do peugeout.
'''

print('Comparativo de Consumo de Combustível')

veiculos = ['fusca','gol', 'uno', 'vectra', 'peugeot']
autonomias = [7, 10, 12.5, 9, 14.5]
litro = 2.25


for i, auto in enumerate(veiculos):
    print(f'Veiculo {i+1}')
    print(f'Nome: {auto}')
    print(f'Km por litro: {autonomias[i]}')


print('\n\nRelatório Final')

for i, auto in enumerate(veiculos):
    milkm = 1000 / autonomias[i]
    gasto = litro * milkm
    print(f'{i+1} - {auto:<10}- {autonomias[i]:>5.1f} -  {milkm:>5.1f} litros - R$ {gasto:>3.2f}')

economico = 0
nome_econo = ''
for i, combust in enumerate(autonomias):
    if combust > economico:
        economico = combust
        nome_econo = veiculos[i]

print(f'O carro mais economico da lista é o {nome_econo}')