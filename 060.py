# FAÇA UM PROGRAMA QUE LEIA UM NUMERO QUALQUER E MOSTRE O SEU FATORIAL.

num = int(input('Insira um numero para que possamos descobrir o seu fatorial: '))
fatorial = 1
contador = num
if num == 0:
    print('O fatorial de 0 é 1')
if num > 0:
    while contador > 0:
        fatorial *= contador
        contador -= 1
    print('O fatorial de {} é {}'.format(num, fatorial))

#SOLUÇÃO DO GUANABARA

from math import factorial
n = int(input('Digite um numero para calcular o seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}'. format(n, f))

print()
print('-=-'*30)
print()

n = int(input('Digite um numero para calcular o seu fatorial: '))
c = n
f = 1
print('Calculando {}!'.format(n))
while c > 0:
    print('{}'.format(c), end=' ')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))



