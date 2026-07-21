'''Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo e seu comprimento. 
Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.
'''

st1 = input('Insira a primeira string: ').strip()
st2 = input('Insira a segunda string: ').strip()

print(f'O tamanho da primeira é de: {len(st1)}')
print(f'O tamanho da segunda é de: {len(st2)}')

print(f'String 1: {st1}')
print(f'String 2: {st2}')

if len(st1) == len(st2):
    print('Sendo assim, as duas possuem o mesmo tamanho!')
else:
    print('Sendo assim, são de tamanhos diferentes!')

if st1 == st2:
    print('As duas strings são iguais!')
else:
    print('As duas strings são diferentes!')