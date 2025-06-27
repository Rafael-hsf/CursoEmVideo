#Crie um porgrama que faça o computador jogar jokenpo com você
from random import randint
from time import sleep
opçoes = ['pedra', 'papel', 'tesoura']
computador = randint(0,2)
jogador = int(input('Essas são as opções \n0. pedra \n1. Papel \n2. Tesoura \nQual jogada você escolhe?  '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=-'*9)
print('computador escolheu {} \njogador escolheu {}'.format(opçoes[computador], opçoes[jogador]))
print('-=-'*9)
print()
if computador == 0:
    if jogador == 0:
        print('EMPATOU!')
    elif jogador == 1:
        print('JOGADOR VENCEU!')
    elif jogador == 2:
        print('COMPUTADOR VENCEU!')
    else:
        print('JOGADA INVALIDA!')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCEU!')
    elif jogador == 1:
        print('EMPATOU!')
    elif jogador == 2:
        print('JOGADOR VENCEU!')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCEU!')
    elif jogador == 1:
        print('COMPUTADOR VENCEU!')
    elif joagdor == 2:
        print('EMPATOU!')
    else:
        print('JOGADA INVALIDA!')




