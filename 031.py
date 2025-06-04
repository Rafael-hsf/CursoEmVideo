#Desenvolva um programa que pergunte a distancia de uma viagem em km. Calcule o preço da passagem cobrando R$0,50 por km
#para viagens de ate 200km e R$0,45 para viagens mais longas

distancia = int(input('quantos km de distancia tem sua viagem ? '))
if distancia <= 200:
    v1 = distancia * 0.50
    print('O valor da sua passagem vai ser R${:.2f}'.format(v1))
else:
    v2 = (distancia * 0.45)
    print('O valor da sua passagem vai ser R${:.2f}'.format(v2))

