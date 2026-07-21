''' Valida e corrige número de telefone. 
Faça um programa que leia um número de telefone, e corrija o número no caso deste conter somente 8 dígitos, acrescentando o '9' na frente. 
O usuário pode informar o número com ou sem o traço separador.
'''

tel = input('Insira o numero de telefone: ').strip()

tel = tel.replace('-', '')

if len(tel) == 9 and tel.isnumeric():
    print(f'Telefone sem formatação: {tel}')
    print(f'Telefone com formatação: {tel[:5]}-{tel[5:]}')

elif len(tel) == 8 and tel.isnumeric():
    novotel = '9' + tel
    print(f'Telefone sem formatação: {novotel}')
    print(f'Telefone com formatação: {novotel[:5]}-{novotel[5:]}')
else:
    print('Numero Invalido!')
    exit() 