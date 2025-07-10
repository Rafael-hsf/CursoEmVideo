#Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares, se o valor digitado for ímpar desconsidere-o
print()
print('-=-'*24)
print('PARA INICIARMOS ESSE PROGRAMA PRECISO QUE ESCOLHA 6 NUMEROS, VAMOS LÁ!')
print('-=-'*24)
soma = 0
n1 = int(input('numero 1: '))
n2 = int(input('numero 2: '))
n3 = int(input('numero 3: '))
n4 = int(input('numero 4: '))
n5 = int(input('numero 5: '))
n6 = int(input('numero 6: '))
lista = [n1, n2, n3, n4, n5, n6]
for c in lista:
    if c % 2 == 0:
        soma += c
print()
print('A soma dos numeros pares dessa lista é: {}'.format(soma))
print()
print('-=-'*30)

# SOLUÇÃO DO GUANABARA

soma = 0
cont = 0
for c in range (1, 7):
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você informou {} números pares e a soma foi {}'.format(cont, soma))