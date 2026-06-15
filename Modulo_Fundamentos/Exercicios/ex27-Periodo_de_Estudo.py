# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
#   Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
  
periodo = input('Em qual periodo voce estuda?\n[M] - MATUTINO\n[V] - VESPERTINO\n[N] - NOTURNO\nInsira a letra correspondente: ').strip().upper()

if periodo == 'M':
    print('Bom Dia!')
elif periodo == 'V':
    print('Boa Tarde!')
elif periodo == 'N':
    print('Boa Noite!')
else:
    print('Entrada inválida! Digite apenas [M] / [V] / [N].')