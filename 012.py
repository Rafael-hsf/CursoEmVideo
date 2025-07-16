# Faça um programa que leia o preço de um produto e mostre seu novo preço com 5% de desconto

pr = float(input('insira o valor do produto: '))
po = float(input('insira a porcentagem de desconto desejada: '))
d = po/100*pr
print(pr-d)