#AULA 12 - CONDIÇÕES ANINHADAS
#
#  IF - se - Abre uma estrutura de condições
#  ELIF - senão se - usado quando existema mais de duas condições a serem testadas (ELIF pode ser usado mais de uma vez em uma estrutura)
#  ELSE - senão - finaliza uma estrutura de condições (a utilização do ELSE pode ser opcional, não é necessario utilizar ele para concluir)

# EXEMPLO:

nome = str(input('Qual é o seu nome? ')).upper()
if nome == 'RAFAEL':
    print('Que nome bonito!')
elif nome == 'PEDRO' or nome == 'MARIA' or nome == 'PAULO':
    print('Seu nome é bem popular no Brasil')
elif nome in 'ANA CLAUDIA JESSICA JULIANA':
    print('Belo nome feminino')
else:
    print('seu nome é bem normal')
print('Tenha um bomo dia {}'.format(nome).title())










