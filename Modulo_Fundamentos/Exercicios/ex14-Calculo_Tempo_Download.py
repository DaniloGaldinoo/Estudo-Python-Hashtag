arq = float(input('Digite o tamanho do arquivo (em MB): '))
vel = float(input('Digite a velocidade da internet (em Mbps): '))

tempo_seg = (arq * 8) / vel
tempo_min = tempo_seg / 60

print(f'Tempo aproximado de download: {tempo_min:.2f} minutos')