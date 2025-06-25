#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele
#foi multado. A multa vai custar R$7,00 por cada km acima do limite.

vel = int(input('Velocidade que o carro passou: '))
if vel <= 80:
    print('Parabens você não recebera uma multa!')
else:
    multa = (vel - 80) * 7.00
    print('Você ultrapassou o limite da via, por isso recera uma multa no valor de R${:.2f}'.format(multa))

print()
print('-=-'*25)
print()


velocidade = float(input('Qual a velocidade atual do carro ? '))
print()
if velocidade > 80:
    print('MULTADO.Você esta acima da velocidade permitida e sera multado por isso')
    multa = (velocidade - 80) * 7.00
    print()
    print('A multa vai ser no valor de R${:.2f}'.format(multa))
    print()
print('Tenha um bom dia, digija com cuidado!')