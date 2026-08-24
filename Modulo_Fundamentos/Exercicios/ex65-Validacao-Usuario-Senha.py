''' Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
mostrando uma mensagem de erro e voltando a pedir as informações.
'''

while True:
    nome = input('Insira o nome de usuário: ')
    senha = input('Insira a senha: ')

    if nome == senha:
        print('O nome de usuário e a senha não podem ser iguais!')
        print('Tente novamente.')
        continue

    print('Usuário e senha cadastrados com sucesso!')
    break