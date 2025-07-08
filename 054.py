#Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas pessoas ainda não atingiram a maioridade
#e quantas ja são maiores

print('-=-~'*20)
print('Para rodarmos esse programa precisamos que nos informe as idades de 7 pessoas')
print('-=-~'*20)
soma = 0
p1 = int(input('Dite a idade da primeira pessoa: '))
p2 = int(input('Dite aidade da segunda pessoa: '))
p3 = int(input('Dite a idade da terceira pessoa: '))
p4 = int(input('Dite a idade da quarta pessoa: '))
p5 = int(input('Dite a idade da quinta pessoa:'))
p6 = int(input('Dite a idade da sexta pessoa: '))
p7 = int(input('Dite a idade da sétima pessoa:'))

list = [p1, p2, p3, p4, p5, p6, p7]
for i in list:
        if i >= 18:
            soma += 1
print()
print('A quantidade de pessoas maiores de idade é: {}\nE a quantidade de menores de idade é: {}'.format(soma, 7 - soma))




