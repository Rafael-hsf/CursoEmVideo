#Refaça o desafio 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for

num = int(input('Digite o numero para o qual você deseja ver a tabuada: '))
for c in range(1, 11):
    print('{} X {:2} = {}'.format(num, c, c*num))