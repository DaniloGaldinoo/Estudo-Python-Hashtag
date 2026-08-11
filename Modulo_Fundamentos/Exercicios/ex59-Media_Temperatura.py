''''Em quais meses a média de temperatura foi maior do que a média nacional?
'''

meses = [
    'Janeiro',
    'Fevereiro',
    'Março',
    'Abril',
    'Maio',
    'Junho',
    'Julho',
    'Agosto',
    'Setembro',
    'Outubro',
    'Novembro',
    'Dezembro'
]

temperaturas = [30, 29, 28, 28, 25, 26, 20, 21, 19, 25, 27, 32]
total_temperaturas = 0

for temperatura in temperaturas:
    total_temperaturas += temperatura

media_temperaturas = total_temperaturas / len(temperaturas)

for i, temperatura in enumerate(temperaturas):
    if temperatura > media_temperaturas:
        print(f'{meses[i]}: {temperatura}°C')
        