# Condições Pt1
#
# se/senão = if/else
#
# if/else - O if testa uma condição e executa uma ação se o teste der true (verdadeiro), o else executa uma ação caso a condição
# testada em if seja (false) falsa. Esse teste vai ser usado em casos em que o programa tenha mais de uma possibilidade, exemplo:
#
#um programa que avalia se o carro é atual ou antigo com base em quantos anos ele tem, acima de tres anos o carro é
#considerado antigo.
#
#tempo = int(input('Quantos anos tem seu carro ?'))
#if tempo <= 3
#   print('seu carro é considerado antigo')
#else
#   print('seu carro é considerado novo')
#print('--FIM--')
#
# DE FORMA SIMPLIFICADA
#
#tempo = int(input('quantos anos tem seu carro ?'))
#print('carro novo' if tempo<=3 else 'carro velho')
#print('--FIM--')
from idlelib.sidebar import EndLineDelegator

nome = str(input('Qual é o seu nome? ')).upper()
if nome == 'RAFAEL':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é bem normal')
print()
print('Bomd dia, {}!'.format(nome.capitalize()))
print()

print(nome.capitalize(), 'vamos calcular a média das suas notas, insira as informações a seguir, por favor: ')
print()
n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))
m = (n1 + n2) / 2
print()
print('A sua média foi {:.1f}'.format(m))
print()
if m >= 6.0:
    print('Sua média foi boa! PARABENS!')
else:
    print('Sua média foi ruim, ESTUDE MAIS!')











































































