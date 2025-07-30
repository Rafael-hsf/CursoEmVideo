# CRIE UM PRGRAMA QUE LEIA A IDADE E O SEXO DE VÁRIAS PESSOAS. A CADA PESSOA CADASTRADA, O PROGRAMA DEVERA PERGUNTAR SE O USUÁRIO QUER OU NÃO CONTINUAR
# NO FINAL MOSTRE:
# A) QUANTAS PESSOAS TEM MAIS DE 18 ANOS
# B) QUANTOS HOMENS FORAM CADASTRADOS
# C) QUANTAS MULHERES TEM MENOS DE 20 ANOS
from time import sleep
maior = homens = mulher20 = 0
while True:
    idade = int(input('Digite a idade da pessoa: '))
    sexo = str(input('Digite o sexo da pessoa: [F/M] ')).strip().upper()[0]
    while sexo not in 'FM':
        sexo = str(input('Digite o sexo da pessoa: [F/M] ')).strip().upper()[0]
    continua = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

    if idade > 18:
        maior += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulher20 += 1
    if continua == 'S':
        print()
        print('-=-'*20)
        print()
        continue
    if continua == 'N':
        print(f'OK, nesse cadastro tivemos: \n{maior} maiores de 18 anos \n{homens} homens cadastrados \n{mulher20} mulheres com menos de 20 anos. ')
        sleep(1)
        print('Agora o programa sera encerrado...')
        break
sleep(2)
print('PROGRAMA ENCERRADO!!')

