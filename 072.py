'''  Crie um programa que tenha um tupla totalmente preenchida com uma contagem por extenso de zero até vinte.
Seu programa deverá ler um numero pelo teclado (entre 0 e 20) e mostra-lo por extenso.
'''

contagem = ('zero', 'um', 'dois', 'três', 'quatro',
            'cinco', 'seis', 'sete', 'oito', 'nove',
            'dez', 'onze', 'doze', 'treze', 'quatorze',
            'quinze', 'dezesseis', 'dezesete', 'dezoito',
            'dezenoveze', 'vinte')
while True:
    while True:
        numero = int(input('Escolha um número entre 0 e 20: '))
        if numero >= 0 and numero <= 20:
            print(f'Você escolheu o numero {numero}, {contagem[numero].upper()}')
            break
        else:
            print('Opção invalida, tente novamente. ', end='')
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        print('Finalizando...')
        break
    else:
        print('Ok, vamos la!', end=' ')


'''SOLUÇÃO DO GUANABARA'''

cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'quatorze',
        'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')
while True:
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        print('Tente novamente.', end='')
    print(f'Você digitou o número {cont[num].upper()}')
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        print('Finalizando...')
        break
    else:
        print('Ok vamos la!', end='')

