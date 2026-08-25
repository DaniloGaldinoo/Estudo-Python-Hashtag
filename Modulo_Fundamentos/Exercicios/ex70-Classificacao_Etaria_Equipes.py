''' Faça um programa que consiga categorizar a idade das equipes de uma empresa. 
Faça um programa que peça para n pessoas a sua idade, ao final o programa devera 
verificar se a média de idade da equipe varia entre 0 e 25 (jovem) ,26 e 60 (sênior) e maior que 60 (idosa); 
e então, dizer se a equipe é jovem, sênior ou idosa, conforme a média calculada.
'''
qtd = int(input('Insira quantas pessoas fazem parte da equipe: '))
qtdd = qtd
idadetotal = 0

while qtd > 0:

    idade = int(input('Informe a idade: '))

    idadetotal += idade
    qtd -= 1

media = idadetotal / qtdd

if media >= 0 and media <=25:
    print(f'Media {media}')
    print ('Equipe JOVEM!')

elif media >= 26 and media <= 60:
    print(f'Media {media}')
    print ('Equipe SENIOR!!')

else:
    print(f'Media {media}')
    print('Equipe IDOSA!')