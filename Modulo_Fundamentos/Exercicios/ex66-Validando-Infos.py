''' Faça um programa que leia e valide as seguintes informações 
(e para cada uma delas, continue pedindo a informação até o usuário inserir corretamente):

Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
'''
nome = ''
idade = 0
sal = 0
sexo = ''
civil = ''

while len(nome) <= 3:
    nome = input('Insira o nome: ')

    if len(nome) <= 3:
        print('O nome deve conter no minimo 4 letras.\nInsira Novamente')

print('Inserido com sucesso.')

while idade < 0 or idade > 150:
    idade = int(input('Insira a idade: '))

    if idade < 0 or idade > 150:
        print('Idade incorreta.\nInsira novamente.')

print('Inserido com sucesso.')

while sal <= 0:
    sal = float(input('Insira o salario: '))

    if sal <= 0:
        print('Salario Incorreto.\nInsira novamente.')

print('Inserido com sucesso.')

while sexo not in ['M', 'F']:
    sexo = input('Insira o sexo: ').upper().strip()

    if sexo not in ['M','F']:
        print('Sexo incorreto.\nInsira novamente.')

print('Inserido com sucesso.')

while civil not in ['S', 'C', 'V', 'D']:
    civil = input('Insira o estado civil: ').upper().strip()

    if civil not in ['S','C','V','D']:
        print('Estado civil incorreto.\nInsira novamente.')

print('Inserido com sucesso.')