#Faça um programa que leia um numero inteiro e diga se ele é ou não um numero primo
num = int(input('Digite um numero para vermos se ele é primo: '))
if num % 2 != 0 and num % 3 != 0:
    print('O numero {} é primo'.format(num))
else:
    print('O numero {} não é primo'.format(num))
