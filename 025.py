#Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome

nome = str(input('digite seu nome completo: '))
nome1 = nome.find('Silva')
print()
if nome1 != -1:
    print('Seu nome tem o nome Silva!')
else:
    print('Seu nome não tem o nome Silva')