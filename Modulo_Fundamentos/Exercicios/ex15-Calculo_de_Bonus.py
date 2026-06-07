# Crie um programa que calcule e dê um print no bonus que os funcionarios devem receber segundo a regra:
# A meta é 1000 vendas.
# Se o valor de vendas for maior ou igual a meta, o valor do bonus do funcionario é de 10% do valor das vendas.
# Caso contrario o valor de bonus do funcionario é 0.
# Print o bonus dos 3 funcionarios.

meta = 1000

while True:
    func1 = int(input("Digite o valor de vendas do funcionario 1: ")) 
    func2 = int(input("Digite o valor de vendas do funcionario 2: "))
    func3 = int(input("Digite o valor de vendas do funcionario 3: "))

    if func1 >= meta:
        bonus1 = func1*0.10
        print(f'O valor das vendas do funcionário 1 foi de R$: {func1:.2f} e seu bonus foi de {bonus1:.2f}')
    else:
        print(f'O funcionário 1 não bateu a meta. Então não possui bonus!')
    if func2 >= meta:
        bonus2 = func2*0.10
        print(f'O valor das vendas do funcionário 2 foi de R$: {func2:.2f} e seu bonus foi de {bonus2:.2f}')
    else:
        print(f'O funcionário 2 não bateu a meta. Então não possui bonus!')
    if func3 >= meta:
        bonus3 = func3*0.10
        print(f'O valor das vendas do funcionário 3 foi de R$: {func3:.2f} e seu bonus foi de {bonus3:.2f}')
    else:
        print(f'O funcionário 3 não bateu a meta. Então não possui bonus!')
    
    resp = str(input('Deseja Continuar? [S/N]')).upper()
    if resp == 'S':
        continue
    else:
        break
print('S A I N D O . . .')
