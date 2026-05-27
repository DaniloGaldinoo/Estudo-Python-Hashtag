altura = float(input('Digite a sua altura (em metros): '))
peso = float(input('Digite o seu peso (em kg): '))
genero = input('Digite o seu gênero (M para masculino, F para feminino): ').upper() 
imc = peso / (altura ** 2)
print(f'O seu IMC é: {imc:.2f}')
if genero == 'M':
    if imc < 20.7:
        print('Abaixo do peso')
    elif 20.7 <= imc < 26.4:
        print('Peso ideal')
    else:
        print('Acima do peso')
elif genero == 'F':
    if imc < 19.1:
        print('Abaixo do peso')
    elif 19.1 <= imc < 25.8:
        print('Peso ideal')
    else:
        print('Acima do peso')
else:
    print('Gênero inválido. Por favor, insira M para masculino ou F para feminino.')
    