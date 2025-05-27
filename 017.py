#Faça um programa que leia o comprimento do cateto oposto e do cateto adjaente de um triangulo retangulo,
# calcule e moste o comprimento da hipotenusa

from math import sqrt
co = float(input('comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente: '))
pt1 = co**2 + ca**2
hi = sqrt(pt1)
print('o comprimento da hipotenusa é {:.2f}'.format(hi))

print('='*50)

from math import hypot
co = float(input('comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('O compirmento da hipotenusa é: {:.2f}'.format(hi))

print('='*50)

co = float(input('comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente: '))
hi = (co**2 + ca**2) ** 0.5
print('O comprimento da hipotenusa <UNK>: {:.2f}'.format(hi))
