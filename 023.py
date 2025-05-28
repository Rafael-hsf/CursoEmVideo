#Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados.
# ex:
# digite um numero: 1834
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1
# tentar fazer como string e matematicamente

num = str(input('digite um numero de 1000 a 9999: '))
print('unidade: {} \ndezena: {} \ncentena: {} \nmilhar: {}'.format(num[3], num[2], num[1], num[0]))




