
# Faça um Programa que verifique o estado civil de uma pessoa. Se a letra digitada é "C" (Casado), "S" (Solteiro), "D" (Divorciado), "V" (Viúvo) ou "O" (outros). Conforme a letra escrita pelo usuário seu programa deve escrever o estado civil.

est = str(input('Qual o seu Estado civil?\n\n[C] = Casado\n[S] = Solteiro\n[D] = Divorciado\n[O] = Outros\n\nInforme a Letra Correspondente: ')).upper()

if est == "C":
    estado = 'Casado'
    print (f'O usuario é {estado}')
elif est == "S":
    estado = 'Solteiro'
    print (f'O usuario é {estado}')
elif est == "D":
    estado = 'Divorciado'
    print (f'O usuario é {estado}')
elif est == "O":
    estado = 'Outros'
    print (f'O usuario é {estado}')
else:
    print('Entrada Invalida!\nFinalizando o Sistema. . .')
