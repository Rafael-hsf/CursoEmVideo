#Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela sua porção inteira
#EX: digite o numero 6.127, a parte inteira desse numero é 6

from math import floor
num = float(input('digite um numero decimal: '))
int = floor(num)
print('A parte inteira do seu numero é: {}'.format(int))

print('='*50)

from math import trunc
num = float(input('digite um numero decimal: '))
print('A parte inteira do seu numero é: {}'.format(trunc(num)))

print('='*50)


