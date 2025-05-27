#FAça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo

import math
angulo = float(input('dgite o angulo que você deseja: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('o angulo {} tem: \nSeno: {:.2f} \nCosseno: {:.2f} \ntangente: {:.2f}'.format(angulo, seno, cosseno, tangente))
