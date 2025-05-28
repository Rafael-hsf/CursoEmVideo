#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra "santo"

cidade = str(input('digite o nome da sua cidade: '))
cidade1 = cidade.split()
print()
if 'Santo' in cidade1[0]:
    print('A cidade começa com a palavra santo')
else:
    print('A cidade não começa com a palavra santo')