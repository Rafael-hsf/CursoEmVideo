# CRIE UM PROGRAMA QUE LEIA O NOME E O PREÇO DE VÁRIOS PRODUTOS. O PROGRAMA DEVERÁ PERGUNTAR SE O USUÁRIO VAI CONTINUAR. NO FINAL, MOSTRE:
# A) QUAL É O TOTAL GASTO NA COMPRA.
# B) QUANTOS PRODUTOS CUSTAM MAIS QUE R$1000.
# C) QUAL É O NOME DO PRODUTO MAIS BARATO.
lista = []
maior = menor = cont = 0
barato = ''
while True:
    produto = str(input('Insira o nome do produto: '))
    valor = float(input('Insira o valor do produto: '))
    cont += 1
    continua = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while continua not in 'SN':
        continua = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    lista.append(valor)
    if valor > 1000:
        maior += 1
    if cont == 1 or valor < menor:
        menor = valor
        barato = produto
    if continua == 'S':
        continue
    if continua == 'N':
        print(f'O total gasto na compra foi de R${sum(lista)}, tendo {maior} produtos com o valor maior que R$1000,00 e o produto mais barato foi o {barato} que custou R${menor}')
        break

#SOLUÇÃO DO GUANABARA

total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Insira o nome do produto: '))
    preço = float(input('Preço: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor: #QUANDO FOR ADICIONADO O PRIMEIRO PRODUTO ENTÃO A VARIAVEL 'MENOR' SERA DEFINIDA COM BASE NELE, MAS SE FOR ADICIONADO ALGUM
        menor = preço              #PRODUTO DE PREÇO MENOR ESSE IRÁ SUBSTITUIR A ATRIBUIÇÃO ANTERIOR DA VARIAVEL 'MENOR', E A VARIAVEL 'BARATO' SEGUE O MESMO RACIOCÍNIO.
        barato = produto
    resp = ''
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi: {total:.2f}')
print(f'Temos {totmil} produtos acima de R$1.000,00')
print(f'Oproduto mais barato foi {barato} que custa R${menor:.2f}')