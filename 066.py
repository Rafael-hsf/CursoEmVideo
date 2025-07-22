# CRIE UM PROGRAMA QUE LEIA VÁRIOS NÚMEROS INTEIROS PELO TECLADO. O PROGRAMA SÓ VAI PARAR QUANDO O USUÁRIO DIGITAR O VALOR 999, QUE É A CONDIÇÃO
# DE PARADA. NO FINAL MOSTRE QUANTOS NÚMEROS FORAM DIGITADOS E QUAL FOI A SOMA ENTRE ELES (DESCONSIDERANDO O FLAG).


n = c = 0
while True:
    num = int(input('Digie um valor: '))
    if num == 999:
        break
    n += num
    c += 1
print(f'Você adicionou {c} números e a soma entre eles é {n}')