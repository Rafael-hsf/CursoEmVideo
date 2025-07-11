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
print('E com {} palpites VOCÊ ACERTOU!!'.format(esc))

