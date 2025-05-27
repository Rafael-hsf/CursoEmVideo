# crie um programa que leia um numero e mostre seu dobro, triplo e raiz quadrada
num = int(input('digite um numero: '))
dob = num * 2
tri = num * 3
raiz = num ** (1/2)
print('numero escolhido: {}'.format(num))
print('dobro: {}'.format(dob))
print('triplo: {}'.format(tri))
print('Raiz quadrada: {:.2f}'.format(raiz))
print('='*35)
n = int(input('digite um numero: '))
d = n * 2
t = n * 3
r = n**(1/2)
print('O dobro de {} é {}. \nO triplo de {} é {}. \nA raiz de {} é {:.2f}.'.format(n, d, n, t, n, r))
print('='*35)
