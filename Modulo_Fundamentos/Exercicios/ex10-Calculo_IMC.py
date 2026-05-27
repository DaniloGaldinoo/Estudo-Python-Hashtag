altura = float(input('Digite a sua altura (em metros): '))
peso = float(input('Digite o seu peso (em quilogramas): '))
imc = peso / (altura ** 2)
print(f'O seu IMC é: {imc:.2f}')