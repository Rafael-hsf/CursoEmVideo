# Crie um programa que leia um numero e me informe o seu antecessor e o seu sucessor
num = int(input("digite um numero: "))
ant = num - 1
suc = num + 1
print('numero escolhido: {}'.format(num))
print('antecessor: {}'.format(ant))
print('sucessor: {}'.format(suc))

num = int(input("por favor insira um numero: "))
print('analisando o numero {} podemos dizer que seu antecessor é {} e seu sucessor é {}'.format(num, (num-1), (num+1)))

