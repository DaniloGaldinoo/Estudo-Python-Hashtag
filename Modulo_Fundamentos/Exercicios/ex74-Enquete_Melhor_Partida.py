''' Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador após cada jogo. 
Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas, para a computação dos votos. 
Sua equipe foi contratada para desenvolver este programa, utilizando a linguagem de programação Python. 
Para computar cada voto, a telefonista digitará um número, entre 1 e 23, correspondente ao número da camisa do jogador. 
Um número de jogador igual zero, indica que a votação foi encerrada. 
Se um número inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número. 
Após o final da votação, o programa deverá exibir:

a. O total de votos computados;
b. Os números e respectivos votos de todos os jogadores que receberam votos;
c. O percentual de votos de cada um destes jogadores;
d. O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual de votos dados a ele.

Observe que os votos inválidos e o zero final não devem ser computados como votos. O resultado aparece ordenado pelo número do jogador. 
O programa deve fazer uso de arrays. 
O programa deverá executar o cálculo do percentual de cada jogador através de uma função. 
Esta função receberá dois parâmetros: o número de votos de um jogador e o total de votos. 
A função calculará o percentual e retornará o valor calculado. 
Abaixo segue uma tela de exemplo. 
A disposição das informações deve ser o mais próxima possível ao exemplo. 
Os dados são fictícios e podem mudar a cada execução do programa. 
Ao final, o programa deve ainda gravar os dados referentes ao resultado da votação em um arquivo texto no disco, 
    obedecendo a mesma disposição apresentada na tela.
```
Enquete: Quem foi o melhor jogador?

Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 11
Número do jogador (0=fim): 10
Número do jogador (0=fim): 50
Informe um valor entre 1 e 23 ou 0 para sair!
Número do jogador (0=fim): 9
Número do jogador (0=fim): 9
Número do jogador (0=fim): 0

Resultado da votação:

Foram computados 8 votos.

Jogador Votos           %
9               4               50,0%
10              3               37,5%
11              1               12,5%

'''

def calcular_percentual(votos, total):
    return (votos / total) * 100


votos = [0] * 24
total_votos = 0

print('Enquete: Quem foi o melhor jogador?\n')

while True:
    jogador = int(input('Número do jogador (0=fim): '))

    if jogador == 0:
        break

    if jogador < 1 or jogador > 23:
        print('Informe um valor entre 1 e 23 ou 0 para sair!\n')
        continue

    votos[jogador] += 1
    total_votos += 1


print('\nResultado da votação:\n')
print(f'Foram computados {total_votos} votos.\n')

if total_votos == 0:
    print('Nenhum voto foi computado.')
else:
    print(f'{"Jogador":<10}{"Votos":<10}%')

    melhor_jogador = 0
    maior_votos = 0

    for jogador in range(1, 24):
        if votos[jogador] > 0:
            percentual = calcular_percentual(votos[jogador], total_votos)

            print(f'{jogador:<10}{votos[jogador]:<10}{percentual:.1f}%')

            if votos[jogador] > maior_votos:
                maior_votos = votos[jogador]
                melhor_jogador = jogador

    percentual_melhor = calcular_percentual(maior_votos, total_votos)

    print('\nO melhor jogador foi:')
    print(f'Jogador: {melhor_jogador}')
    print(f'Votos: {maior_votos}')
    print(f'Percentual: {percentual_melhor:.1f}%')