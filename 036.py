#Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. O programa vai perguntar o valor da casa
#o salario do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ele nao pode exceder 30%
#do salario ou então o emprestimo sera negado.

nome = str(input('Informe seu nome: '))
print('Olá {}, vamos avaliar as possibilidades do seu financiamento'.format(nome).title())
print('=~='*30)
casa = float(input('{}, qual o valor da casa? R$'.format(nome).title()))
print()
renda = float(input('{}, por favor nos informe sua renda: R$'.format(nome).title()))
print()
parcelas = int(input('Agora {}, nos informe em quantos anos você pretende pagar esse emprestimo: '.format(nome).title()))
vp = casa / (parcelas * 12)
if vp <= renda * 0.3:
    print('O valor da sua prestação mensal ficara em: R${:.2f} então sera possivel prosseguir com o financiamento, PARABENS!'.format(vp))
else:
    print('O valor da sua prestação mensal ficara em R${:.2f}, infelizmente não sera possivel prossegui com o financiamento'.format(vp))
