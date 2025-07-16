#REFAÇA O EXERCICIO 51 LENDO O PRIMEIRO TERMO E A RAZÃO DE UMA PROGRSSÃO ARITIMETICA, MOSTRANDO OS 10 PRIMEIROS TERMOS
#DA PROGRESSÃO USANDO A ESTRUTURA WHILE

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
contador = 1
print('Os 10 primeiros termos da PA são:')

while contador < 11:
    print('{}'.format(primeiro), end = ' → ')
    primeiro += razão
    contador += 1
print('FIM!!')