#Faça um programa que leia um numero inteiro e diga se ele é ou não um numero primo
num = int(input('Digite um numero para vermos se ele é primo: '))
if num % 2 != 0 and num % 3 != 0:
    print('O numero {} é primo'.format(num))
else:
    print('O numero {} não é primo'.format(num))
print()
print('-=-'*30)
print()

# SOLUÇÃO DO GUANABARA

num = int(input('Diigite um numero: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('E por isso ele é primo!')
else:
    print('E por isso ele não é primo!')
