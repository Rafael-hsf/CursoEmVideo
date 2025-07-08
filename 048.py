#FAça um programa que calcule a soma entre todos os números ímpares que são múltiplos de 3 e que se encontram no intervalo de 1 até 500
soma = 0
for c in range(1, 501):
    if c % 3 == 0 and not c % 2 == 0:
         soma += c
print()
print("a soma dos numeros ímpares multiplos de 3 entre 1 e 500 é: {}.".format(soma))
print()
print('-=-'*30)
print()
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print('A soma de todos os {} valore solicitador é {}.'.format(cont, soma))

