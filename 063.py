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

    #SOLUÇÃO DO GUANABARA

    n = int(input('Quantos termos da sequencia de fibonacci você quer mostrar ? '))
    t1 = 0
    t2 = 1
    print()
    print('{} → {}'. format(t1, t2), end=' ')
    cont = 3
    while cont <= n:
        t3 = t1 + t2
        print(' → {}'.format(t3), end=' ')
        t1 = t2
        t2 = t3
        cont += 1
    print('FIM!')


