# MELHORE O JOGO DO DESAFIO 28 AONDE O COMPUTADOR VAI PENSAR EM UM NÚMERO ENTRE 0 E 10. SÓ QUE AGORA O JOGADOR VAI TENTAR
# ADIVINHAR ATÉ ACERTAR, MOSTRANDO NO FINAL QUANTOS PALPITES FORAM NECESSÁRIOS PARA GANHAR.

from random import randint
esc = 0
num = randint(1, 10)
escolha = int(input('Tente acertar o numero que o computador escolheu entre 1 e 10: '))
if escolha != num:
    esc += 1
while escolha != num:
    if escolha != num:
        esc += 1

    print('Escolha errada!')
    escolha = int(input('Tente novamente: '))
print()
print('E com {} palpites VOCÊ ACERTOU!!'.format(esc))
print('-=-'*30)

#SOLUÇÃO DO GUANABARA

from random import randint
computador =  randint(1, 10)
print('Sou seu computador, acabei de pensar em um numero de 0 a 10, sera que você consegue adivinhar qual é ?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite ? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente novamente!')
        else:
            print('Menos... Tente novamente!')
print('Acertou com {} tentativas'.format(palpites))


