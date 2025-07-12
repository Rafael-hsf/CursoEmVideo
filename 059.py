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


