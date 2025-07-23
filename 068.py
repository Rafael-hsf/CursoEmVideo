# FAÇA UM PROGRAMA QUE JOGUE PAR OU ÍMPAR COM O COMPUTADOR. O JOGO SERA INTERROMPIDO QUANDO O JOGADOR PERDER, MOSTRANDO O TOTAL DE VITÓRIAS CONSECUTIVAS
# QUE ELE CONQUISTOU NO FINAL DO JOGO.
from random import randint
print('-=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=-'*20)
num = contador = 0
par = num % 2 == 0
impar = num % 2 != 0
while True:
    computador = randint(1, 10)
    while True:
        escolha = str(input('Você escolhe para ou impar ? [P/I] ')).upper().strip()
        print()
        if escolha in ('P', 'I'):
            if escolha == 'P':
                escolha = par
            if escolha == 'I':
                escolha = impar
            break
        else:
            print('Escolha inválida, tente novamente...')
    print()
    valor = int(input('Agora digite um valor para jogarmos: '))
    while True:
        num += computador + valor
        resultado = impar or par
        if num % 2 == 0:
            resultado = par
        if num % 2 != 0:
            resultado = impar
        else:
            print()
        if escolha == resultado:
            contador += 1
            print(f'A soma entre a sua escolha e a do computador foi de {num} então VOCÊ GANHOU!!')
            break
        else:
            print(f'A soma entre a sua escolha e a do computador foi de {num} então você perdeu...')
            print(f'E com um total de {contador} vitórias consecutivas o jogo esta finalizado...')
print('-=-'*20)










