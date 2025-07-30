# CRIE UM PROGRAMA QUE LEIA O NOME E O PREÇO DE VÁRIOS PRODUTOS. O PROGRAMA DEVERÁ PERGUNTAR SE O USUÁRIO VAI CONTINUAR. NO FINAL, MOSTRE:
# A) QUAL É O TOTAL GASTO NA COMPRA.
# B) QUANTOS PRODUTOS CUSTAM MAIS QUE R$1000.
# C) QUAL É O NOME DO PRODUTO MAIS BARATO.
lista = []
maior = 0
while True:
    produto = str(input('Insira o nome do produto: '))
    valor = float(input('Insira o valor do produto: '))
    continua = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while continua not in 'SN':
        continua = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    lista.append(valor)
    if valor > 1000:
        maior += 1
    if continua == 'S':
        continue
    if continua == 'N':
        print(f'O total gasto na compra foi de {sum(lista)}, tendo {maior} produtos com o valor maior que R$1000,00 e o produto mais barato foi o ...')
        break



