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

    if idade >= 18:
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
        print(f'OK, nesse cadastro tivemos: \n{maior} pessoas maiores de 18 anos \n{homens} homens cadastrados \n{mulher20} mulheres com menos de 20 anos. ')
        sleep(1)
        print('Agora o programa sera encerrado...')
        break
sleep(2)
print('PROGRAMA ENCERRADO!!')


#SOLUÇÃO DO GUANABARA
tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ''
    while sexo not in 'FM':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1

    resp = ''
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados')
print(f'E temos {totM20} mulheres com menos de 20 anos')
