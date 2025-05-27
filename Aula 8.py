# Aprendendo a trabalhar com modulos
# Os modulos adicionam funções ao python que não estão presentes na sua forma base.
# Comando "import" para utilizar os modulos, para utilizar funções unicas ao inves de importar a lista de funções completas pode se usar o "from"
# Exemplos: "import(modulo X)" ou "from (modulo X) import (função especifica)"
# Modulo math (matematica) funções:
# ceil: arredonda um numero pra cima
# floor : arredonda um numero pra baixo
# trunch : trunca um numero
# pow: potencia
#sqrt : raiz quadrada
# factorial : fatoração
#EXEMPLO PRATICO

import math
#Arredondando pra cima
num = int(input("por favor insira um numero: "))
raiz = math.sqrt(num)
print('a raiz de {} é igual a: {}'.format(num, math.ceil(raiz)))

print('='*30)

#Arredondando pra baixo
num = int(input('por favor insira um numero: '))
raiz = math.sqrt(num)
print('a raiz de {} é igual a {}'.format(num, math.floor(raiz)))

print('='*30)

#Sem arredondar
num = int(input('por favor insira um numero: '))
raiz = math.sqrt(num)
print('a raiz de {} é igual a {:.2f}'.format(num, raiz))

print('='*30)

#importando funções especificas

from math import sqrt, floor, ceil
num = int(input('por favor insira um numero: '))
raiz = sqrt(num)
print('a raiz de {} é igual a {:.2f}'.format(num, raiz))

print('='*30)

num = int(input('por favor insira um numero: '))
raiz = sqrt(num)
print('a raiz de {} é igual a {}'.format(num, ceil(raiz)))

print('='*30)

num = int(input('por favor insira um numero: '))
raiz = sqrt(num)
print('a raiz de {} é igual a {}'.format(num, floor(raiz)))

print('='*30)

import emoji
from math import ceil
num = float(input('por favor insira sua nota 1'))
num2 = float(input('por favor insira sua nota 2'))
media = (num + num2) / 2
print('sua média é de: {}1'.format(media))

