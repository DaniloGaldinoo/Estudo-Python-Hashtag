''' Faça um programa que peça uma nota, entre zero e dez. 
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
'''

while True:
    n = input('Insira um numero entre ZERO e DEZ: ')

    if n < 0 or n > 10:
        print('Entrada Incorreta, tente novamente.')
        continue
    else:
        print('Valor inserido corretamente. Finalizando o Programa!')
        break
