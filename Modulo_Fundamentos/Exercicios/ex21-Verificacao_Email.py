# Faça um programa que verifique se o e-mail digitado faz parte dos e-mail de spam.
#   SPAM = ('fulano@gmail.com', 'beltrano@gmail.com', 'ciclano@gmail.com')

while True:
    mail = str(input('Insira seu e-mail: ')).lower()

    if mail in ('fulano@gmail.com', 'beltrano@gmail.com', 'ciclano@gmail.com'):
        print ('Esse e-mail não pode ser usado. Tente novamente!')
    else:
        print ('E-mail salvo com sucesso!')
        break