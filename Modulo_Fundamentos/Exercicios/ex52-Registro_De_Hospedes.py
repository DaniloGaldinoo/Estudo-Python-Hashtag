''' Criando um Registro de Hóspedes

Digamos que você está criando o sistema para registrar a chegada de hóspedes em um hotel. 
No hotel, os hóspedes podem ter quartos com 1, 2, 3 e 4 pessoas. 

Seu sistema deve conseguir:
1. Identificar quantas pessoas o hóspede que acabou de chegar vai ter no quarto (perguntando por meio de input)
2. De acordo com a quantidade de pessoas do hóspede, ele deve fazer um for para perguntar o cpf e o nome de cada 
    pessoa, a fim de registrá-la no quarto (2 inputs para cada pessoa, 1 para o cpf e outro para o nome)
3. O seu programa então deve gerar duas listas com todas as pessoas que ficarão no quarto em que 
    as duas listas consigam correlacionar os indices no futuro
- Para simplificar, não vamos nos preocupar com possibilidades de "tentar colocar mais de 1 hóspede, 
    digitar o cpf errado, etc. Nosso objetivo é treinar a criação de uma rotina de cadastro
'''

hospedes = int(input('Insira quantas pessoas vão ficar no quarto: '))
nomes = []
cpfs = []

for i in range (hospedes):
    nome = input(f'Insira o nome do {i+1}º hospede: ')
    cpf = input(f'Insira o CPF do {i+1}º Hospede: ')
    nomes.append(nome)
    cpfs.append(cpf)
