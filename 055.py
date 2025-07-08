#Faça um programa que leia o peso de cinco pessoas. No final mostre qual foi o maior e o menor peso lidos

print('POR FAVOR INFORME O PESO DAS PESSOAS DO TESTE')
p1 = float(input('infome o peso da pessoa 1: '))
p2 = float(input('infome o peso da pessoa 2: '))
p3 = float(input('infome o peso da pessoa 3: '))
p4 = float(input('infome o peso da pessoa 4: '))
p5 = float(input('infome o peso da pessoa 5: '))

lista = [p1, p2, p3, p4, p5]
maior = max(lista)
menor = min(lista)

print('O maior peso da lista é {}kg e o menor é {}kg'.format(maior, menor))