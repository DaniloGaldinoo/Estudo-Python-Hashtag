import math

area = float(input('Informe o tamanho da área a ser pintada em m²: '))

litros_tinta = area / 6

# 1 - Apenas latas

latas = math.ceil(litros_tinta / 18)
preco_latas = latas * 80

print('\n1 - Apenas latas')
print(f'Quantidade de latas: {latas}')
print(f'Preço: R$ {preco_latas:.2f}')

# 2 - Apenas galões

galoes = math.ceil(litros_tinta / 3.6)
preco_galoes = galoes * 25

print('\n2 - Apenas galões')
print(f'Quantidade de galões: {galoes}')
print(f'Preço: R$ {preco_galoes:.2f}')

# 3 - Mistura de latas e galões

litros_tinta = litros_tinta * 1.10

latas = litros_tinta // 18
resto = litros_tinta % 18

galoes = math.ceil(resto / 3.6)

if galoes > 3:
    latas += 1
    galoes = 0

preco_total = (latas * 80) + (galoes * 25)

print('\n3 - Mistura de latas e galões')
print(f'Latas: {int(latas)}')
print(f'Galões: {galoes}')
print(f'Preço: R$ {preco_total:.2f}')