'''  Crie um programa que tenha um tupla totalmente preenchida com uma contagem por extenso de zero até vinte.
Seu programa deverá ler um numero pelo teclado (entre 0 e 20) e mostra-lo por extenso.
'''

contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenoveze', 'vinte')
while True:
    numero = int(input('Escolha um número entre 0 e 20: '))
    if numero in (0, 20):
        print(f'Você escolheu o numero {numero}, {contagem[numero].upper()}')
        break
    else:
        print('Opção invalida, por favor insira um numero entre 0 e 20')





