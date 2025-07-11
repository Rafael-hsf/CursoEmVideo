# ESTRUTURA DE REPETIÇÃO WHILE

# A ESTRUTURA WHILE VAI REPETIR UM COMANDO ATÉ CHEGAR A UM CERTO PONTO QUE FOR DEFINIDO, ENTÃO ENQUANTO NAO CHEGAR AO OBJETIVO
# O PROGRAMA CONTINUA RODANDO A REPETIÇÃO. EX:

#  WHILE NOT MAÇÃ:
#     PASSO
#  PEGA

# ESSE PROGRAMA VAI RODAR FAZENDO COM QUE O PERSONAGEM DE UM PASSO ATÉ CHEGAR A MAÇÃ, ENQUANTO NÃO CHEGAR O COMANDO PASSO
# VAI SE REPETINDO, QUANDO CHEGAR, ELE EXECUTA O COMANDO PEGA.

# WHILE NOT MAÇÃ:
#   IF CHÃO:
#       PASSO
#   IF BURACO:
#       PULA
#   IF MOEDA:
#       PEGA
# PEGA

# ESSE PROGRAMA VAI RODAR FAZENDO COM QUE O PERSONAGEM ANDE ATÉ CHEGAR A MAÇÃ COM CONDIÇÕES ATÉ CHEGAR AO OBJETIVO, ESSAS
# CONDIÇÕES SÃO, SE TIVER CHÃO A FRENTE, DE UM PASSO, SE TIVER UM BURACO A FRENTE, PULE, E SE TIVER UMA MOEDA, A PEGUE.

# PRÁTICA

for c in range (1, 10):
    print (c)
print('FIM')

print()
print()

c = 1
while c < 10:
    print(c)
    c = c + 1
print('FIM')

print()
print('-=-'*30)
print()

for c in range(1, 5):
    n = int(input('Digite um valor: '))
print('FIM')

print()
print()

r = S
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar ? [S/N] ')).upper()
print('FIM')

print()
print('-=-'*30)
print()

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} numeros pares e {} numeros ímpares!'.format(par, impar))