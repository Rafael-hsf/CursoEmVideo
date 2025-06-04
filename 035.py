#Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou não formar um triangulo
from tokenize import endpats

reta1 = float(input('Digite o valor da reta 1: '))
reta2 = float(input('Digite o valor da reta 2: '))
reta3 = float(input('Digite o valor da reta 3: '))
s1 = reta1 + reta2
s2 = reta1 + reta3
s3 = reta3 + reta2
lista = [s1, s2, s3]

for valor in lista:
    if valor <= 0:
        print('Não é possivel criar um triangulo com essas retas')
    else:
        print('É possivel criar um triangulo com essas retas')