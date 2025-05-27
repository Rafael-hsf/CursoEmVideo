from math import ceil
num = float(input('por favor insira sua nota 1 '))
num2 = float(input('por favor insira sua nota 2 '))
res = (num + num2) / 2
media = ceil(res)
print('sua média é de: {:.2f}'.format(media))
