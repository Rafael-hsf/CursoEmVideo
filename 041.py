#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria
#de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 20 anos: SENIOR
# Acima: MASTER

idade = int(input('Insira a idade do competidor: '))
print()
if idade <= 9:
    print('Este é um competidor MIRIM')
elif 9 < idade <= 14:
    print('Este é um competidor INFANTIL')
elif 14 < idade <= 19:
    print('Este é um competidor JUNIOR')
elif 19 < idade <= 20:
    print('Este é um competidor SENIOR')
elif idade > 20:
    print('Este é um competidor MASTER')