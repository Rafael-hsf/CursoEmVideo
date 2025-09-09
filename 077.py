'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos). depois disso você deve mostrar para cada palavra quais são suas vogais'''

palavras = []
palavra = str(input('Digite uma palavra: '))
palavras.append(palavra)
while True:
    continuar = str(input('Deseja continuar? [S/N]: ')).strip()[0].upper()
    if continuar == 'N':
        break
    if continuar == 'S':
        palavra1 = str(input('Digite mais uma palavra: '))
        palavras.append(palavra1)
    if continuar not in ['S', 'N']:
        print('Digite apenas com sim ou não.')
print('Finalizando ...')

tupla = tuple(palavras)
for p in tupla:
    vogais = []
    for letra in p:
        if letra.lower() in 'aeiou':
            vogais.append(letra)
    if vogais:
        print(f'na palavra {p} tem as vogais {' '.join(vogais)}')
    else:
        print(f'A palavra {p} não possui vogais')


