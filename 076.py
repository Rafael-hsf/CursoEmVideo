'''Crie um programa que tenha uma tupla unica com nomes de produtos e seus respectivos preços na sequência
No final mostre uma listagem de preços, organizando os dados em uma forma tabular'''
from time import sleep
lista = []
while True:
    produto = str(input('Digite o nome do produto: '))
    valor = float(input('Digite o valor do produto: '))
    lista_completa  = [produto, valor]
    lista.append(lista_completa)
    while True:
        continuar = str(input('Deseja adicionar mais produtos? [S/N]: ')).upper().strip()[0]
        if continuar not in 'SN':
            print("Você escolheu uma opção invalida, por favor escolha entre sim ou não [S/N]")
        else:
            break
    if continuar == 'N':
        break
    else:
        continue

lista1 = tuple(lista)
sleep(2)
print('\n--- TABELA DE PRODUTOS ---')
print(f'{"PRODUTO":<20} {"VALOR (R$)":>12}')
print('-'*33)
total = 0
for item in lista1:
    produto = item[0]
    valor = item[1]
    print(f'{produto:<20} {valor:>12.2f}')
    total += valor
print('-'*33)
print(f'{"TOTAL":<20} {total:>12.2f}')
print("-"*33)


