#Escreva um programa que leia dois numeros inteiros e compare-os mostrando na tela uma das seguintes mensagem:
#O primeiro valor é maior
#O segundo valor é menor
#Não existe valor maior, os dois são iguais

num1 = int(input('Digie um numero: '))
num2 = int(input('Digite outro numero: '))
if num1 > num2:
    print('O primeiro numero é maior que o segundo numero')
elif num2 > num1:
    print('O segundo numero é maior que o primeiro numero')
else:
    print('Não existe valor maior, os dois são iguais')