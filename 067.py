# FAÇA UM PROGRAMA QUE MOSTRE A TABUADA DE VÁRIOS NÚMEROS, UM DE CADA VEZ, PARA CADA VALOR DIGITADO PELO USUÁRIO. O PROGRAMA SERÁ INTERROMPIDO QUANDO
# O NÚMERO SOLICITADO FOR NEGATIVO.

while True:
    print('--x--'*10)
    num = int(input('Digite um numero para vermos sua tabuada: '))
    if num < 0:
        break
    else:
        for c in range(1, 11):
            print(f'{num} X {c:2} = {num * c:2}')
print('FIM!!')

#SOLUÇÃO DO GUANABARA


while True:
    n = int(input('Quer ver a tabuada de qual valor ? '))
    if n < 0:
        break
    print('-'*30)
    for c in range(1, 11):
        print(f'{n} X {c:2} = {n * c:2}')
    print('-'*30)
print('PROGRAMA DE TABUADA ENCERRADO!!')