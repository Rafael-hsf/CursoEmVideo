#Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome

nome = str(input('digite seu nome completo: '))
nome1 = nome.find('Silva')
print()
if nome1 != -1:
    print('Seu nome tem Silva!')
else:
    print('Seu nome não tem Silva')

print()
print('='*50)
print()

nome = str(input('digite seu nome completo: '))
print('Seu nome tem Silva ? {}'.format('silva' in nome.lower()))