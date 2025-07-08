#Crie um programa que mostre todos os numeros pares no intervalo entre 1 e 50
from time import sleep
for c in range(2, 51, 2):
    print(c, end=' ')
    sleep(0.5)
print('FIM')