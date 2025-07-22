# FAÇA UM PROGRAMA QUE JOGUE PAR OU ÍMPAR COM O COMPUTADOR. O JOGO SERA INTERROMPIDO QUANDO O JOGADOR PERDER, MOSTRANDO O TOTAL DE VITÓRIAS CONSECUTIVAS
# QUE ELE CONQUISTOU NO FINAL DO JOGO.
from random import randint
print('-=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=-'*20)
computador = randint(1, 10)
jogador = str(input('Você escolha para ou ímpar ? [P/I] ')).upper()
while jogador not in 'PpIi':
    print('Resposta invalida, tente novamente')
num = int(input('Agora escolha o seu numero: '))
resultado = computador + num


