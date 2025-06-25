#Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade:
#Se ele ainda vai se alistar ao serviço militar
#Se é a hora de se alistar no serviço militar
#Se ja passou o ano do alistamento
#
#Seu programa tambem deve mostrar o tempo que falta ou que passou do prazo

from datetime import date
nascimento = int(input('Informe em qual ano você nasceu: '))
ano_atual = date.today().year
idade = ano_atual - nascimento
print()
if idade < 18:
    print('Você ainda nao esta em idade de se alistar, ainda faltam {} anos'.format(18 - idade))
elif idade == 18:
    print('Você esta na idade exata para se alistar')
else:
    print('Você ja passou da idade de se alistar, ja passou {} anos do prazo'.format(idade - 18))