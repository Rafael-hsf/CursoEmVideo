''' Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla, e no final mostre:
a) quantas vezes aparece o valor 9
b) em que posição foi digitado o primeiro valor 3.
c) quais foram os números pares
'''

n1 = int(input('informe o primeiro valor: '))
n2 = int(input('informe o segundo valor: '))
n3 = int(input('informe o terceiro valor: '))
n4 = int(input('informe o quarto valor: '))

#Armazenando os numeros em uma tupla
numeros = (n1, n2, n3, n4)

#Quantas vezes aparece o 9
if 9 in numeros:
    cont9 = numeros.count(9)
    print(f'O número 9 apareceu {cont9} vezes')
else:
    print('O número 9 não aparece nessa lista')

#Em que posição foi digitado o primeiro valor 3
if 3 in numeros:
    pos3 = numeros.index(3)
    print(f'O número 3 apareceu primeiro na posição {pos3 + 1}')
else:
    print('O número 3 não aparece nesssa lista')

#Quais foram os numeros pares
pares = []
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
pares = tuple(pares)
print(f'Os numeros pares que apareceram foram: {pares}')