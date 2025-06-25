#Escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual sera a base da conversão:
# 1 para binario
# 2 para octal
# 3 para hexadecimal

num = int(input('Por favor insira um numero: '))
print()
escolha = int(input('Agora de acordo com as seguintes opções: \n1. binario \n2. octal \n3. hexadecimal \nEscolha em qual base você quer que eu converta o numero: '))
print()
if escolha == 1:
    print('O numero {} em binario é {}'.format(num, bin(num)[2:]))
elif escolha == 2:
    print('O numero {} em octal é {}'.format(num, oct(num)[2:]))
else:
    print('O numero {} em hexadecimal é {}'.format(num, hex(num)[2:]))