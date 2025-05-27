# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias que ele foi alugado.
#Calcule o preço a pagar sabendo que o carro custa 60,00 por dia e 0,15 por km rodado.
dias = int(input('por quantos dias o carro foi alugado ? '))
km = float(input('quantos km ele rodou durante o aluguel ? '))
vd = dias * 60
vk = km * 0.15
vt = vd + vk
print()
print('tendo sido alugado por {} dias e rodado {}km, o custo ficou o seguinte \nvalor por dia alugado: R${:.2f} \nValor por km rodado: R${:.2f} \nValor total: R${:.2f}'.format(dias, km, vd, vk, vt))
print()
print('=' * 40)
# Outra forma de resolver
print()

dias = int(input('por quantos dias o carro foi alugado ? '))
km = float(input('quantos km ele rodou durante o aluguel ? '))
pg = (dias * 60) + (km *0.15)
print('o total a ser pago é de: R${:.2f}'.format(pg))
