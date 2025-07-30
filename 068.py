# FAÇA UM PROGRAMA QUE JOGUE PAR OU ÍMPAR COM O COMPUTADOR. O JOGO SERA INTERROMPIDO QUANDO O JOGADOR PERDER, MOSTRANDO O TOTAL DE VITÓRIAS CONSECUTIVAS
# QUE ELE CONQUISTOU NO FINAL DO JOGO.
from random import randint
vitorias = 0
while True:
    jogador = int(input('Escolha seu valor: '))
    computador = randint(1, 10)
    total = jogador + computador
    escolha = str(input('Você escolhe par ou ímpar? [P/I] ')).strip().upper()[0]
    while escolha not in 'PpIi':
        esolha = str(input('Você escolhe par ou ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador} e o total {total} ')
    if escolha == 'P':
        if total % 2 == 0:
            print(f'Você venceu, vamos para a próxima. ')
            vitorias += 1
        else:
            print('Você perdeu, o jogo sera finalizado...')
            break
    elif escolha == 'I':
        if total % 2 == 1:
            print('Você venceu, vamos para a próxima. ')
            vitorias += 1
        else:
            print('Você perdeu, o jogo sera finalizado...')
            break
print(f'JOGO ENCERRADO! você venceu {vitorias} vezes.')

#SOLUÇÃO DO GUANABARA

from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total}  ')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
print(f'GAME OVER! Você venceu {v} vezes.')














