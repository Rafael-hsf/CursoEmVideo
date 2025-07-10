#Desenvolva um programa que leia o primeiro termo e a razão de uma Progressão Aritimética. No final mostre os 10 primeiros
#termos dessa progressão
from sys import exit
termo = int(input('digite o numero que iniciara a progressão aritimetica: '))
valor = int(input('Agora informe o valor da razão: '))
for c in range(termo, 11, valor):
    print('{}'.format(c))
print()
print('-=-'*30)
print()

# SOLUÇÃO DO GUANABARA

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razão
for c in range (primeiro, decimo + razão, razão):
    print('{}'.format(c), end=' → ')
print('ACABOU')
