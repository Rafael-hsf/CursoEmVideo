#ESCREVA UM PROGRAMA QUE LEIA UM NUMERO N INTEIRO QUALQUER E MOSTRE NA TELA OS N PRIMEIROS ELEMENTOS DE UMA
#SEQUENCIA DE FIBONACCI.

num = int(input('Digite um numero para descobrirmos sua sequencia de fibonacci: '))
anterior = 0
atual = 1
contador = 0
elementos = int(input('Quantos elementos você quer que essa sequencia apresente ? '))
if num <= 0:
    print('Por favor insira um numero positivo.')
while contador < elementos:
    proximo = anterior + atual
    print(proximo)
    anterior = proximo
    atual = proximo
    contador += 1


