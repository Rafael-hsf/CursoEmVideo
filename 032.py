#Faça um programa que leia um ano qualquer e mostre se ele é bissexto

ano = int(input('Qual ano você quer analisar ? '))
bi = ano % 4
if bi == 0:
    print('Esse ano é bissexto')
else:
    print('Esse ano não é bissexto')

print()
print('-=-'*25)
print()

from datetime import date
ano = int(input('Qual ano você quer analisar ? Coloque 0 para analisar o ano atual:  '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} não é BISSEXTO'.format(ano))