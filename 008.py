# Crie um programa que receba um valor em metros e converta ela para centimetros e milimetro
m = float(input('insira a medida em metros que você deseja converter: '))
cm = m * 100
mm = m* 1000
print()
print('centimetros: {}'.format(cm))
print('milimetros: {}'.format(mm))