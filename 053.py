#Crie um programa que leia uma frase e diga se ela é um palindromo, desconsiderando os espaços

frase = str(input('Digite uma frase para vermos se ela é um palindromo: ')).lower().split()
frase1 = ''.join(frase)
invertida = frase1[::-1]

if frase1 == invertida:
    print('Essa frase é um palindromo!!')
else:
    print('Essa frase não é um palindromo!')
