#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente

nome = str(input('Digite seu nome completo: ')).strip()
nome1 = nome.split()
print('O primeiro nome é {}, e o ultimo nome é {}'.format(nome1[0], nome1[-1]))

print()
print('='*50)
print()

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[len(nome)-1]))


