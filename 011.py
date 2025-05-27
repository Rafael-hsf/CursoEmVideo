# Faça um programa que leia a altura e largura de uma parede, calcule sua area e a quantidade de tinta necessaria para pinta-la,
# sabendo que cada litro de tinta pinta 2m²

a = float(input('digite a altura da parede: '))
l = float(input('digite a largura da parede: '))
ar = a*l
print()
print('a area da sua parede é de {} m²'.format(ar))
print()
tinta = ar/2
print('para pintar sua parede sera necessário {} litros de tinta'.format(tinta))

