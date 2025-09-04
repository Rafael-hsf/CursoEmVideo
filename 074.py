''' Crie um programa que vai gerar 5 números aleatórios e colocar em uma tupla.
Depois disso mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
'''

from random import randint
n1 = randint(1, 1000)
n2 = randint(1, 1000)
n3 = randint(1, 1000)
n4 = randint(1, 1000)
n5 = randint(1, 1000)

numeros = (n1, n2, n3, n4, n5)
print(f'os numeros gerados foram: {numeros} \nSendo o maior {max(numeros)} e o menor {min(numeros)}')

