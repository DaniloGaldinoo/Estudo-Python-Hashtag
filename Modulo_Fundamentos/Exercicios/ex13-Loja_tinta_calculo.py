print ('*'*30)
print ('Loja de Tinta Galdino!')
print ('*'*30)

area = float(input('Digite a área a ser pintada (em metros quadrados): '))
litros = area / 3
latas = litros / 18
preco = latas * 80  
print(f'Quantidade de tinta necessária: {litros:.2f} litros')
print(f'Número de latas necessárias: {latas:.2f} latas')
print(f'Preço total: R$ {preco:.2f}')

