#Desenvolva uma logica que leia o peso e altura de uma pessoa, calcule seu imc e mostre seu status, de acordo com a tabela abaixo:
# abaixo de 18.5: abaixo do peso
# entre 18.5 e 25: peso ideal
# 25 ate 30: sobrepeso
# 30 ate 40: obesidade
# acima de 40: obesidade morbida
print()
print('\033[7;30;41m-=-\033[0m'*30)
print('             OLÁ ESSE É UM SISTEMA PARA CALCULAR O SEU IMC, VAMOS COMEÇAR!')
print('\033[7;30;41m-=-\033[0m'*30)
print()
nome = str(input('Para iniciarmos, por gentileza me informe seu nome: ')).upper()
print()
peso = float(input('Por favor me informe seu peso: '))
altura = float(input('Por favor informe sua altura: '))
imc = peso / (altura ** 2)
print()
if imc <= 18.5:
    print('{}, seu IMC é de {:.2f}, isso significa que você esta abaixo do peso, procure um nutricionista.'.format(nome.title(), imc))
elif imc > 18.5 and imc <= 25:
    print('{}, seu IMC é de {:.2f}, isso significa que você esta dentro do peso ideal, mantenha assim!'.format(nome.title(), imc))
elif imc > 25 and imc <= 30:
    print('{}, seu IMC é de {:.2f}, isso significa que você esta com sobrepeso, melhore a dieta e pratique exercicios'.format(nome.title(), imc))
elif imc > 30 and imc <= 40:
    print('{}, seu IMC é de {:.2f}, isso significa que você esta com obesidade, procure um endocrinologista.'.format(nome.title(), imc))
else:
    print('{}, seu IMC é de {:.2f}, isso significa que você esta com obesidade morbida, procure um endocrinologista.'.format(nome.title(), imc))