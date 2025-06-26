#Refaça o desafio 035 dos triangulos acrescentando o recurso de mostrar que tipo de triangulo sera formado:
# Equilatero: todos os lados iguais
# Isóceles: dois lados iguais
# Escaleno: todos os lados diferentes

reta1 = float(input('insira o valor da reta 1: '))
reta2 = float(input('insira o valor da reta 2: '))
reta3 = float(input('insira o valor da reta 3: '))
s1 = reta1 + reta2
s2 = reta1 + reta3
s3 = reta2 + reta2
lista = [s1, s2, s3]

for valor in lista:
    if valor <= 0:
        print('Não é possivel montar um triagulo com essas medidas')
    elif valor > 0 and reta1 == reta2 == reta3:
        print('É possivel montar um tringulo equilatero com essas medidas!')
    elif valor > 0 and reta1 != reta2 and reta1 != reta3:
        print('É possivel montar um triangulo escaleno com essas medidas!')
    elif valor > 0 and reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print('É possivel monstar um triangulo isóceles com essas medidas!')
    else:
        print()



