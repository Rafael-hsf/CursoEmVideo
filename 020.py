#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho do alunos.
#Faça um programa que leia o nome dos quadtro alunos e mostre a ordem sorteada
import random

a1 = str(input('aluno 1: '))
a2 = str(input('aluno 2: '))
a3 = str(input('aluno 3: '))
a4 = str(input('aluno 4: '))
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('a ordem de apresentação é a seguinte: {}'.format(lista))