#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele
#foi multado. A multa vai custar R$7,00 por cada km acima do limite.

vel = int(input('Velocidade que o carro passou: '))
if vel <= 80:
    print('Parabens você não recebera uma multa!')
else:
    multa = (vel - 80) * 7.00
    print('Você ultrapassou o limite da via, por isso recera uma multa no valor de R${:.2f}'.format(multa))