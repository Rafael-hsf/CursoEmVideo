# Faça um programa que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento

s = float(input('insira o valor do seu salário: '))
p = float(input('insira a porcentagem de aumento: '))
ns = p/100*s
a = s+ns
print()
print('O salário corrigido é: R${}'.format(a))

