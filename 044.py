#Elabore um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e condição de pagamento
# A vista dinheiro/cheque: 10% de desconto
# A vistaa no cartão: 5% de desconto
# Em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros
print()
valor = float(input('Qual o valor do produto? R$'))
print()
pagamento = int(input('Selecione a forma de pagamento que você pretende utilizar: \n1. Dinheiro \n2. Cartão á vista \n3. Cartão até 2x \n4. Cartão 3x ou mais \n '))
print()
if pagamento == 1:
    print('Com o pagamento em dinheiro você tera um desconto de 10% e o valor final ficara em R${:.2f}'.format(valor - (valor * 10 / 100)))
elif pagamento == 2:
    print('Com o pagamento a vista no cartão você tera um desconto de 5% e o valor final ficara em R${:.2f}'.format(valor -(valor * 5 / 100)))
elif pagamento == 3:
    print('Com o pagamento em até 2x no crediro o valor fica normal, o valor final fica em R${}'.format(valor))
else:
    print('Em compras parceladas em 3x ou mais havera um acrescimo de 20%, o valor final ficara em R${:.2f}'.format(valor + (valor * 20 / 100)))