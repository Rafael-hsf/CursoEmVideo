#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparecem a letra A
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece a ultima vez

texto = str(input('digite uma frase: ')).upper().strip()
print('o texto tem {} letras A'.format(texto.count('A')))
print('a primeira letra a do texto aparece pela primeira vez na posição: {}'.format(texto.find('A')))
print('e a ultima vez que ela aparece é na posição: {}'.format(texto.rfind('A')))

print()
print('='*50)
print()

frase = str(input('digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A ultima letra A aparece na posição {}'.format(frase.rfind('A')+1))


