#Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiusculas
# - O nome com todas as letras minusculas
# - Quantas letras no total, sem considerar os espaços
# - Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: '))
print(nome.upper())
print(nome.lower())
nome1 = nome.split()
nome1 = ('').join(nome1)
print('o nome tem {} letras'.format(len(nome1)))
nome2 = nome.split()
print('o primeiro nome tem {} letras'.format(len(nome2[0])))

print()
print('='*50)
print()

nome = str(input('Digite seu nome completo: ')).strip()
print('analisando seu nome...')
print('seu nome em maiusculas é {}'.format(nome.upper()))
print('seu nome em minusculas é {}'.format(nome.lower()))
print('seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
#print('seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('seu pirmeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))



