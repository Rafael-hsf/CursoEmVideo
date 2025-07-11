# CRIE UM PROGRAMA QUE LEIA DOIS VALORES E MOSTRE UM MENU NA TELA:
# [1] SOMAR
# [2] MULTIPLICAR
# [3] MAIOR
# [4] NOVOS NÚMEROS
# [5] SAIR DO PROGRAMA
# SEU PROGRAMA DEVERÁ REALIZAR A OPERAÇÃO SOLICITADA EM CADA CASO.

while escolha == (1, 5):
    num1 = int(input('Informe o primeiro valor: '))
    num2 = int(input('Informe o segundo valor: '))
    print('Agora escolha uma opção para darmos continuidade:')
    escolha = int(input('[1] Somar \n[2] Multiplicar \n[3] Maior numero \n[4] Escolher novos numeros \n[5] Encerrar programa \n'))
    print()
            if escolha == 1:
                print('A soma dos numeros escolhidos é igual a {}'.format(num1 + num2))
            if escolha == 2:
                print('A multiplicação dos numeros escolhidos é igual a {}'.format(num1 * num2))
            if escolha == 3:
                print('O maior numero entre os numeros informados é {}'.format(max(num1, num2)))
            if escolha == 4:
                num1 = int(input('Informe o primeiro valor: '))
                num2 = int(input('Informe o segundo valor: '))
                print('Agora escolha uma opção para darmos continuidade: ')
                escolha = int(input('[1] Somar \n[2] Multiplicar \n[3] Maior numero \n[4] Escolher novos numeros \n[5] Encerrar programa \n'))
            if escolha == 5:
                print('Encerrando o programa...')


