#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra "santo"

cidade = str(input('digite o nome da sua cidade: ')).strip()
cidade1 = cidade.split()
print()
if 'SANTO' in cidade1[0].upper():
    print('A cidade começa com a palavra santo')
else:
    print('A cidade não começa com a palavra santo')

print()
print('='*50)
print()

cid = str(input('Em qual cidade você nasceu ? ')).strip()
print(cid[:5].upper == 'SANTO')