''' Numa eleição existem três candidatos. 
Faça um programa que peça o número total de eleitores. 
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
'''

eleitores = int(input('Informe a quantidade de eleitores: '))
c1 = 0
c2 = 0
c3 = 0

while eleitores != 0:
    print('Olá Eleitor!\nEssas são as opções de voto:')
    print('[1] - Candidato 1')
    print('[2] - Candidato 2')
    print('[3] - Candidato 3')

    voto = int(input('Informe o seu voto: '))

    if voto == 1:
        c1 += 1
        eleitores -= 1
    elif voto == 2:
        c2 += 1
        eleitores -= 1

    elif voto == 3:
        c3 += 1
        eleitores -= 1

    else:
        print('Voto Incorreto!\n Tente Novamente.')
        continue

print('Eleição Encerrada!')
print('O resultado foi o seguinte:')
print(f'Candidato 1 = {c1} votos')
print(f'Candidato 2 = {c2} votos')
print(f'Candidato 3 = {c3} votos')

if c1 == c2 == c3:
     print('Empate entre os tres!')
elif c1 == c2 and c1 > c3:
     print('Empate entre os candidatos 1 e 2!')
elif c1 == c3 and c1 > c2:
     print('Empate entre os candidatos 1 e 3!')
elif c2 == c3 and c2 > c1:
     print('Empate entre os candidatos 2 e 3!')
elif c1 > c2 and c1 > c3:
    print(f'O VENCEDOR FOI O CANDIDATO 1! COM {c1} VOTOS!!')
elif c2 > c1 and c2 > c3:
        print(f'O VENCEDOR FOI O CANDIDATO 2! COM {c2} VOTOS!!')
else:
         print(f'O VENCEDOR FOI O CANDIDATO 3! COM {c3} VOTOS!!')