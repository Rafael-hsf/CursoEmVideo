#CRIE UM PROGRAMA QUE LEIA VARIOS NUMEROS INTEIROS PELO TECLADO. O PROGRAMA SÓ VAI PARAR QUANDO O USUÁRIO DIGITAR O
#VALOR 999, QUE É A CONDIÇÃO DE PARADA, NO FINAL MOSTRE QUANTOS NÚMEROS FORAM DIGITADOS E QUAL FOI A SOMA ENTRE ELES
#(DESCONSIDERANDO O FLAG)
contador = 0
total = 0
print('Precisamos que você adicione os numeros que deseja somar, e para concluir as adições basta digitar 999.')
print()
while True:
    valor = int(input('digite o numero que você deseja acrescentar a soma: '))
    print()
    if valor == 999:
        break
    total += valor
    contador += 1
print('Você digitou {} numeros e a soma de todos eles é igual a {}'.format(contador, total))

print('FIM')

#SOLUÇÃO DO GUANABARA

num = cont = soma = 0
num = int(input('Digite um numero [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um numero [999 para parar]: '))
print('Você digitou {} números e a soma foi {}'.format(cont, soma))

