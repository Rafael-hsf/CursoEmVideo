#Crie um programa que leia um numero inteiro e mostre na tela se ele é par ou impar

num = int(input('insira um numero: '))
n = num % 2
if n == 0:
    print('o numero é par')
else:
    print('o numero é impar')