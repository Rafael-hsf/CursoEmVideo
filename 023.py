#Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados.
# ex:
# digite um numero: 1834
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1
# tentar fazer como string e matematicamente

#num = str(input('digite um numero de 0 a 9999: '))
#print('unidade: {} \ndezena: {} \ncentena: {} \nmilhar: {}'.format(num[3], num[2], num[1], num[0]))

print()
print('='*50)
print()

#num = int(input('insira um numero: '))
#n = str(num)
#print('analisando o numero {}'.format(num))
#print('unidade {}'.format(n[3]))
#print('dezena {}'.format(n[2]))
#print('centena {}'.format(n[1]))
#print('milhar {}'.format(n[0]))

print()
print('='*50)
print()

num = int(input('insira um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('analisando o numero {}'.format(num))
print('unidade {}'.format(u))
print('dezena {}'.format(d))
print('centena {}'.format(c))
print('milhar {}'.format(m))



