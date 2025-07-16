#CRIE UM PROGRAMA QUE LEIA VARIOS NUMEROS INTEIROS PELO TECLADO. NO FINAL DA EXECUÇÃO, MOSTRE A MÉDIA ENTRE TODOS OS
#VALORES E QUAL FOI O MAIOR E MENOR VALOR LIDO. O PROGRAMA DEVE PERGUNTAR AO USUÁRIO SE ELE QUER OU NÃO CONTINUAR A DIGITAR VALORES.

print('-=-'*21)
print('Insira os números para que possamos fazer a média entre eles')
print('-=-'*21)
print()
lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    continuar = str(input('Deseja continuar? [S/N] ')).upper()
    print()
    if continuar == 'N':
        break
    else:
        continue
media = sum(lista) / len(lista)
maior = max(lista)
menor = min(lista)
print()
print('A Média entre os valores que você inseriu é {}, o maior valor foi {} e o menor valor foi {}'.format(media, maior, menor))

