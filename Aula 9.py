#AULA 9 - MANIPULANDO TEXTO
#
# * No python textos são 'strings (str)'

# * Sempre que adicionamos um texto ao python, esse texto vai ocupar um pequeno espaço na memoria do computador,
#   e seus caracteres vão ocupar mini espaços dentro desse pequeno espaço.

# * Cada um dos mini espaços vão receber um indice, que é um numero sequencial, que sempre se inicia em 0.
#
# Exemplo: texto = 'AULA 09'
#                   0123456

# * Todos os caracteres possuem uma numeração dentro desse indice, inclusive os espaços entre as palavras.

# FATIAMENTO DE STRINGS

# * O fatiamento de strings é a possibilidade de poder selecionar partes especificas do texto, podendo ser apenas um caracter.

# * Para isso é necessario dizer o nome da variavel e o indice entre colchetes.
#
# Exemplos :  - texto[3] - vai retornar a leta A, pois é a letra que esta no indice 3 do exemplo.
#             - texto[0:3] - vai retornar a palavra AUL, pois o python exclui o ultimo indice, então se você quiser pegar
#               uma palavra completa no fatiamento é preciso colocar sempre um indice a mais na solicitação.
#             - texto[0:4] - Nesse caso vai retornar a palavra AULA.
#             ** NO CASO DE PRECISAR PEGAR A ULTIMA LETRA VOCÊ PODE COLOCAR UM INDICE A MAIS PARA QUE A ULTIMA LETRA NÃO SEJA EXCLUIDA.

# * Dentro do fatiamento tem a possibilidade de você pedir ao python que ele te retorne uma sequencia de indices ignorando
#  alguns indices.
#
# Exemplo: texto[0:7:2] - Nesse caso ele vai trazer os caracteres do 0 ao 6 (0:7) pulando sempre de dois em dois(:2), então ele me traria
#                         'AL 9' ignorando os caracteres 'UA0'

# * Podemos tambem solicitar o fatiamento no python ignorando o primeiro indice no pedido, isso somente nos momento em que esse fatiamento
#   for iniciar no indice 0.
#
# Exemplo: texto[:4] - vai retornar a palavra AULA, pois o indice se inciara no 0 e finalizara no 4, porem o 4 é excluido finalizando no
#          indice 3.

# * Seguindo a mesma logica do exemplo anterior podemos tambem fazer o contrario que seria ignorar o ultimo indice do pedido, quando for
#   finalizar no ultimo indice da frase.
#     ** ESSA FORMA DE FINALIZR NO ULTIMO INDICE É MAIS RECOMENDADA QUE A OUTRA FORMA QUE FOI CITADA QUE SERIA INSERINDO UM NUMERO A MAIS
#     NO FINAL DO INDICE.
#
# Exemplo: [5:] - Vai retornar os caracteres '09', pois se inicia no indice 5 e vai até o final da frase.

# * Podemos tambem otimizar a pedida de fatiamento misturando as formas, por exemplo pedir de um indice especifico até o final, pulando de
# dois em dois.
#
# Exemplo: texto[1::2] - vai retornar 'UA0', pois inciou no indice 1  (1), foi ate o final da frase (1:) e pulou de dois em dois indices (:2)

# ANALISE DE STRING

# * função len - len(texto) - vai retornar a quantidade de caracteres tem na string.
#
# Exemplo: len(texto) = 7

# * função count - usado para descobrir quantas letras especificas tem na sua string.
#
# Exemplo: print(texto.count('A')) = 2
#          print(texto.count('A', 0, 3)) = 1 - função count co fatiamento, vai retornar, quantas letras 'A' tem do indice 0 até o indice 3
#                                   ou seja 1 apenas, porque o indice 3 é excluido no fatiamento.
#          print(texto.count('A', 0, 4)) = 2 - nesse caso vai retornar 2 letras 'A' pois o indice que foi excluido foi o 4 que se refere ao espaço.

# * Função find - print(texto.find('ULA')) - vai retornar o numero do indice do primeiro caracter da palavra pedida no find.
#   quando você coloca uma string que não existe função selecionada vai retornar -1
#
# Exemplo: print(texto.find('ULA')) = 1 - na frase solicitada os caracteres 'ULA' se inciam no indice 1, então essa solicitação me retorna o 1

# * Função in - Essa função é usada para descobris se existe uma string especifica no texto.
#
# Exemplo: 'AULA' in texto = true - nesse caso ele retornou verdadeiro para a pergunta se existe a string aula na função texto

# TRANSFORMAÇÃO

# * Função replace - usada para substituir uma string,
#
# Exemplo: texto.replace('AULA', 'CURSO') = 'CURSO 09' - nesse caso ele substituiu a palavra 'AULA' por 'CURSO', e no caso de ter mais de
# uma palavra igual no texto, todas serão substituidas.

# * Função upper - Essa função deixa a frase inteira em letras maiúsculas.
#
# Exemplo: texto = 'Aula 09'
#          texto.upper() = 'AULA 09'

# * Função lower - O contrário da anterior, deixa a frase inteira em letras minusculas.
#
# Exemplo: texto = 'Aula 09'
#          texto.lower() = 'aula 09'

# * Função capilize - deixa a frase inteira em minusculo e somente a primeira letra em maiúsculo.
#
# Exemplo: texto = 'Aula Python 09'
#          texto.capitalize() = 'Aula python 09'

# * Função title - sempre que houver um espaço a palavra vai inciar com letra maiuscula.
#
# Exemplo: texto = 'Aula de python 09'
#          texto.title = 'Aula De Python 09'

# * Função strip - remove os espaços inuteis no inicio e no final da string
#
# Exemplo: texto = '  Aula de python 09 '
#          texto.strip = 'Aula de python 09'
#   ** Essa função tem variações que são 'rstrip' ou seja 'right strip', que apaga o espaço inutil apenas a direita da string
#      e o 'lstrip' ou seja 'left strip' que apaga o espaço inutil apenas a esquerdada string

# DIVISÃO

# * Função split - Separa as palavras de uma frase de acordo com os espaços, e cada palavra vai ter seu proprio indice,
#   a função split gera uma lista de palavras a partir da função selecionada.
#
# Exemplo: texto = 'aula python'
#          indice - 012345678910
#     texto.split - 'aula python'
#           indice - 0123 012345
#            lista -  p1    p2        (p1 - palavra 1, p2 - palavra 2)

# * Função join - Usada para unir elementos de frase que estão separados no formato do exemplo acima (split).
#
# Exemplo: texto = 'aula python'
#          indice - 012345678910
#      texto.split - 'aula python'
#            indice - 0123 012345
#   '-'.join(texto) - 'aula-python'
#             indice - 012345678910
#  ** O ELEMENTO DETRO DAS ASPAS PODE MUDAR DE ACORDO COM A SUA NECESSIDADE, SE VOCÊ QUISER UNIR A FRASE SEM O '-' DEIXANDO APENAS O ESPAÇO
#     BASTA VOCÊ DEIXAR UM ESPAÇO EM BRANCO ENTRE AS ASPAS (' ').


# PRATICA

frase = '  Curso em video Python  '
print (frase)
print('='*50)

#FATIAR
print('FATIAR')
print (frase[3])
print (frase[3:9])
print(frase[:15])
print(frase[6:])
print(frase[0::2])
print(frase[::2])
print('='*50)

print('ANALISE')
print(len(frase))
print(frase.count('o'))
print(frase.find('video'))
print(frase.find('Videos'))
print('video' in frase)
print('='*50)

print('TRANSFORMAÇÃO')
print(frase.replace('Curso', 'Aula'))
#Para salvar a troca feita com o replace precisa colocar o comando "frase = frase.replace('Curso', 'Aula')", se deixar somente no print
#a alteração não fica salva.
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.strip())
print(frase.lstrip())
print(frase.rstrip())
print('='*50)

print('DIVISÃO')
print(frase.split())
print('-'.join(frase))
print('-'.join(frase.strip()))
print('-'.join(frase.split()))
print(' '.join(frase.strip().split()))
