# FAÇA UM PROGRAMA QUE LEIA UM NUMERO QUALQUER E MOSTRE O SEU FATORIAL.

num = int(input('Insira um numero para que possamos descobrir o seu fatorial: '))
fatorial = 1
contador = num
if num == 0:
    print('O fatorial de 0 é 1')
if num > 0:
    while contador > 0:
        fatorial *= contador
        contador -= 1
    print('O fatorial de {} é {}'.format(num, fatorial))





