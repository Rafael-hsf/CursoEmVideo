#Faça um programa que leia um ano qualquer e mostre se ele é bissexto

ano = int(input('Digite o ano: '))
bi = ano % 4
if bi == 0:
    print('Esse ano é bissexto')
else:
    print('Esse ano não é bissexto')