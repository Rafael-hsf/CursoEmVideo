#Escreva um programa que faça o computador 'pensar' em um numero de 0 a 5 e peça para o usuario tentear descobrir
#qual foi o numero escolhido pelo computador. O programa devera escrever na tela se o usuario venceu ou perdeu.

import random
lista = (1, 2, 3, 4, 5)
num = int(input('Escolha um numero de 1 a 5 e teste sua sorte: '))
sort = random.choice(lista)
print('O numero sorteado foi: {}'.format(sort))
if num == sort:
    print('Parabens você acertou o numero sorteado!')
else:
    print('Que pena você errou, mas tente outra vez!')

print()
print('='*80)
print()

from random import randint
from time import sleep
computador = randint(1, 5) #Faz o computadr pensar
print('-=-'*20)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-'*20)

jogador = int(input('Em que numero eu pensei ? ')) #Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS. Você conseguiu me vencer!')
else:
    print('GANHEI. Eu pensei no numero {} e não no numero{}'.format(computador, jogador))
