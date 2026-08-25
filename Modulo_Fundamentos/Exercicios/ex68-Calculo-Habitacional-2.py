while True:
    # População do país A
    while True:
        PaisA = int(input('Insira a população do país A: '))

        if PaisA <= 0:
            print('A população deve ser maior que zero. Tente novamente.')
        else:
            break

    # Taxa de crescimento do país A
    while True:
        taxaA = float(input('Insira a taxa de crescimento do país A (%): '))

        if taxaA <= 0:
            print('A taxa deve ser maior que zero. Tente novamente.')
        else:
            break

    # População do país B
    while True:
        PaisB = int(input('Insira a população do país B: '))

        if PaisB <= 0:
            print('A população deve ser maior que zero. Tente novamente.')
        else:
            break

    # Taxa de crescimento do país B
    while True:
        taxaB = float(input('Insira a taxa de crescimento do país B (%): '))

        if taxaB <= 0:
            print('A taxa deve ser maior que zero. Tente novamente.')
        else:
            break

    # Transformando as taxas de porcentagem em decimal
    taxaA = taxaA / 100
    taxaB = taxaB / 100

    ano = 0

    # Calculando o número de anos
    while PaisA < PaisB:
        CalcA = PaisA * taxaA
        CalcB = PaisB * taxaB

        PaisA += CalcA
        PaisB += CalcB

        ano += 1

    print(f'\nSerão necessários {ano} anos.')
    print(f'População A = {PaisA:,.2f}')
    print(f'População B = {PaisB:,.2f}')

    # Pergunta se o usuário deseja repetir
    repetir = input('\nDeseja realizar outra operação? (s/n): ').lower().strip()

    if repetir != 's':
        print('Programa encerrado.')
        break