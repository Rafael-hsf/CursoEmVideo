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



