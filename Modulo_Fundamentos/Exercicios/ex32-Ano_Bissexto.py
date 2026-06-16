'''Você está construindo um calendário para controlar dias de trabalho a pedido do RH. 
Nessa construção, você vai precisar definir quais anos são bissextos e quais não são, para montar o calendário de forma correta. 
Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

Dica para determinar se um ano é bissexto: 
- São bissextos todos os anos múltiplos de 400, p.ex.: 1600, 2000, 2400, 2800...
- São bissextos todos os múltiplos de 4, exceto se for múltiplo de 100 mas não de 400, 
p.ex.: 1996, 2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028...
- Não são bissextos todos os demais anos.
ex1: 2004 é múltiplo de 4, mas não é múltiplo de 100, então é bissexto.
ex2: 2000 é múltiplo de 4, mas é múltiplo de 100, só que também é multiplo de 400, então é bissexto (porque todo ano múltiplo de 400 é bissexto, independente do resto).
ex3: 1900 é múltiplo de 4, é múltiplo de 100, mas não é múltiplo de 400, então não é bissexto

Dica: lembre que: numero % 4 é o resto da divisão do número por 4, ex: 10 % 3 = 1 (já que 10/3 = 3 e resta 1)
'''

ano = int(input('Informe o ano que deseja consultar se é ou não Bissexto: '))

if ano % 400 == 0:
    print(f'{ano} é Bissexto!')
elif ano % 100 == 0:
    print(f'{ano} não é Bissexto!')
elif ano % 4 == 0:
    print(f'{ano} é Bissexto!')
else:
    print(f'{ano} não é Bissexto!')


