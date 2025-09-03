''' Crie uma tupla com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de colocação, depois mostre:
a) apenas os 5 primeiros colocados
b) os ultimos 4 colocados da tabela
c) uma lista com os times em ordem alfabética
d) Em que posição da tabela esta o time do São Paulo
'''

brasileiro = ('Flamengo', 'Cruzeiro', 'Palmeiras', 'Bahia', 'Botafogo', 'Mirassol', 'São Paulo', 'Bragantino', 'Fluminense', 'Internacional', 'Ceara', 'Corinthians', 'Grêmio', 'Atletico MG', 'Vasco', 'Santos', 'Vitoria', 'Juventude', 'Fortaleza', 'Sport')
print(f'Os 5 primeiros colocados são: {brasileiro[:5]}')
print(f'Os 4 ultimos colocados são: {brasileiro[-4:]}')
print(f'Em ordem alfabética: {sorted(brasileiro)}')
posição = brasileiro.index('São Paulo')
print(f'O São Paulo esta na posição: {posição + 1}')
