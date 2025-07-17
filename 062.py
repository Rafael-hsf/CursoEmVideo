#MELHORE O DESAFIO 61, PERGUNTANDO PARA O USUARIO SE ELE QUER MOSTRAR MAIS ALGUNS TERMOS. O PROGRAMA TERMINA QUANDO
#ELE DISSER QUE QUER MOSTRAR 0 TERMOS.

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
contador = 1
print()
print('Os 10 primeiros termos da PA são:')

while contador < 11:
    print('{}'.format(primeiro), end = ' → ')
    primeiro += razão
    contador += 1
print()
mais = str(input('\nVocê deseja ver mais termos ? [S/N]: ')).upper()
if mais == 'S':
    print()
    total = int(input('Quantos termos você deseja ver no total ? '))
    print()
    print('Os próximos termos da PA são: ')
    while contador < total + 1:
        print('{}'.format(primeiro),  end = ' → ')
        primeiro += razão
        contador += 1
else:
    print()
print('FIM!!')

#SOLUÇÃO DO GUANABARA

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razã da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} → '. format(termo), end=' ')
        termo += razão
        cont += 1
    print('pausa')
    mais = int(input('Quantos termos você quer mostrar mais ? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
