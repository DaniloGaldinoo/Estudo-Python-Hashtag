# Crie um novo codigo que calcule e de um print no bonus dos funcionarios.
# A meta é 1000 vendas
# Os funcionarios que venderem muito acima da meta ganham mais bonus do que os outros; Entao o bonus é definido assim:
# Se as vendas funcionario for maior ou igual a 2000, então o bonus é de 15% sobre o valor da venda.
# Se for menor que 2000 e maior ou igual a 1000, entao bonus de 10%
# Se for menor que 1000, entao nao tem bonus.

nfunc = 1
while True:

    for funcionario in range (1,4):
        valorvenda = int(input(f"Digite o valor de vendas do funcionario {nfunc}: ")) 
        nfunc += 1
        if valorvenda >= 2000:
            print (f'Funcionario Otimo! O bonus é de 15%, que corresponde a: R$: {valorvenda * 0.15}')
        elif valorvenda < 2000 and valorvenda >= 1000:
            print (f'Funcionario acima da média! O bonus é de 10%, que corresponde a: R$: {valorvenda * 0.10}')
        else:
            print ('Funcionario Precisa melhorar. Infelizmente não alcançou a meta; e não teve bonus!')

    
    resp = str(input('Deseja Continuar? [S/N]')).upper()
    if resp == 'S':
        continue
    else:
        break
print('S A I N D O . . .')