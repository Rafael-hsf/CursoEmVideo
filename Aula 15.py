# INTERROMPENDO REPETIÇÕES WHILE

# BREAK - O comando break é utilizado em laços de repetição como o while para interromper a repetição no meio e desviar o código para fora do laço. exemplo:

# while True: - while true abre um loop infinito.
#   if terra:
#       passo
#   if buraco:
#       pula
#   if maçã:
#       pega
#   if trofeu:
#       pula
#       break - ## Esse break diz que quando o personagem chegar ao troféu ele deve pular para o troféu e concluir o laço pegando o troféu.
# pega
#
# PRÁTICA


n = s = 0
while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    s += n
print(f'A soma dos valores é {s}')

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
