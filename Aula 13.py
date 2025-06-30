#  LAÇOS DE REPETIÇÃO - PARTE 1
#
# Laços de repetição são formas de fazer um certo comando se repetir diversas vezes.
# Laços com variavel de controle - um laço com uma variavel que quando o comando chegar nela a repetição se encerra.
# Exemplo: Um jogo bidimencional onde o personagem se move um bloco a cada passo até chegar a um objeto e pega-lo

# ANDANDO POR 10 BLOCOS ATÉ CHEGAR AO OBJETO
#  for c in range(0,10): - laço for
#     passo - comando do laço (dar um passo repetidamente até chegar no objeto)
#  pega (pegar o objeto e finalizar o laço)

# AGORA NESSES 10 BLOCOS, A CADA DOIS BLOCOS HAVERÁ UM BURACO QUE DEVERÁ SER PULADO ATÉ CHEGAR AO OBJETO
#  for c in range(0,3):
#     passo (dar um passo)
#     pula (apos dar um passo, dar um pulo)
#  passo (dar um passo)
#  pega (pegar o objeto)
# (O comando passo, pula se repetira 3x até chegar ao objeto e o programa executar o comando passo, pega)

# AGORA O MESMO COMANDO DO EXEMPLO ANTERIOR, POREM COM A MISSÃO DE PEGAR AS MOEDAS QUE APARECEREM TAMBÉM
# for c in range(0,3)
#   if moeda (comando if dentro de um laço for)
#      pega (se tiver uma moeda no caminho, pegar)
#   passo
#   pula
# passo
# pega


#PARTE PRÁTICA

for c in range(0, 6) #SE VOCÊ QUISER QUE O COMANDO SE REPITA 6 VEZES VOCÊ PRECISA COLOCAR DE 0 A 6, PORQUE SE VOCÊ COLOCAR DE 1 A 6 ELE VAI REPETIR APENAS 5 VEZES, IGNORANDO A ULTIMA
    print('Oi')
print('FIM')

for c in range(0, 6) #JA NA CONTAGEM SE VOCÊ INICIAR DO 0 A CONTAGEM VAI SE INICIAR NO 0, SE QUISER QUE INICIE NO 1 VAI PRECISAR INICIAR COM 1 E FINALIZAR COM UM AMAIS, EX: CONTAR DE 1 A 5 - (1, 6)
    print(c)
print('FIM')

n = int(input('digite um numero: '))
for c in range(0, n+1)
    print(c)
print('FIM')

i = int(input('inicio: '))
f = int(input('fim: '))
p = int(input('passo: '))
for c in range(i, f+1, p): #Nesse comando a contagem vai ser realizada do inicio ao fim de acordo com a quantidade de passos estipulado. Exemplo, de 0 a 100 contando de 10 em 10
    print(c)
print('FIM')

for c in range(0, 3)
    n = int(input('digite um valor: ')) #Nesse comando o programa vai pedir pra o usuario inserir o valor a quantidade de vezes estipulada, nesse caso 3.
print('FIM')

s = 0
for c in range(0, 4):
    n = int(input('digite um valor: '))
    s += n #Nessa função o programa vai somar todos os valores
print('O somatório de todos os valores é de {}'.format(s))

