# CRIE UM PROGRAMA QUE LEIA DOIS VALORES E MOSTRE UM MENU NA TELA:
# [1] SOMAR
# [2] MULTIPLICAR
# [3] MAIOR
# [4] NOVOS NÚMEROS
# [5] SAIR DO PROGRAMA
# SEU PROGRAMA DEVERÁ REALIZAR A OPERAÇÃO SOLICITADA EM CADA CASO.

while True:
    num1 = int(input('Informe o primeiro valor: '))
    num2 = int(input('Informe o segundo valor: '))
    print('Agora escolha uma opção para darmos continuidade:')


    while True:
        escolha = int(input('[1] Somar \n[2] Multiplicar \n[3] Maior numero \n[4] Escolher novos números \n[5] Encerrar programa \n'))
        if escolha not in [1,2,3,4,5]:
            print('Opção invalida, por favor escolha um numero ente 1 e 5.')

        print()
        if escolha == 1:
            print('A soma entre os dois números é igual a {}'.format(num1 + num2))
            break
        if escolha == 2:
            print('A multiplicação de {} por {} é igual a {}'.format(num1, num2, num1 * num2))
            break
        if escolha == 3:
            if num1 > num2:
                print('O maior número é o {}'.format(num1))
            elif num1 == num2:
                print('Os dois números são iguais.')
            else:
                print('O maior numero é o {}'.format(num2))
            break
        if escolha == 4:
            print('Reiniciando... selecione novos numeros.')
            break
        if escolha == 5:
            print('Encerrando o programa...')
            break
    if escolha == 5 or escolha in (1, 2, 3):
        break

print('FIM!!')

#SOLUÇÃO DO GUANABARA

from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''   [1] somar
    [2] multiplicar
    [3] maior
    [4] novos numeros
    [5] encerrar programa''')
    opção = int(input('Qual é a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print('O resultado de {} X {} é {}'.format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior é {}'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os numeros novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção invalida, tente novamente')
    print('-=-'*30)
    sleep(2)
print('Fim do programa! Volte sempre!')


