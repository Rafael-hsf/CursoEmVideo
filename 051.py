#Desenvolva um programa que leia o primeiro termo e a razão de uma Progressão Aritimética. No final mostre os 10 primeiros
#termos dessa progressão
from sys import exit
termo = int(input('digite o numero que iniciara a progressão aritimetica: '))
print('agora preciso que você me indique se a razão vai ser positiva ou negativa, selecione: \n[1] positiva \n[2] negativa')
razao = int(input())
if razao != 1 and razao != 2:
    print('Opção invalida')
exit()
valor = int(input('Agora informe o valor da razão: '))
for c in range(1, 11):
    if razao == 1:
        termo += valor
        (print(termo))
    elif razao == 2:
        termo -= valor
        print(termo)
    else:
        print('Opção invalida')