#Faça um programa que leia o salario de um funcionario e calcule o valor do seu aumento. Para salarios superiores a
#R$1250,00 calcule um aumento de 10%. Para os inferiores ou iguais o aumento é de 15%

salario = float(input('Insira seu salario '))
if salario <= 1250:
    aumento1 = (15 / 100 * salario) + salario
    print('Seu salario com aumento fica em: R${}'.format(aumento1))
else:
    aumento2 = (10 / 100 * salario) + salario
    print('Seu salario com aumento fica em: R${}'.format(aumento2))
