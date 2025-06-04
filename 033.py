#Faça um programa que leia tres numeros e mostre qual é o maior e qual é o menor.

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
num3 = int(input('Digite mais um numero: '))
print()
lista = [num1, num2, num3]

maior = max(lista)
menor = min(lista)

print('O maior numero da lista é o {}, e o menor é o: {}'.format(maior, menor))