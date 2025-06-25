#Crie um progrma que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final de acordo com a media atingida
# Media abaixo de 5.0 REPROVADO
# Media entre 5.0 e 6.9 RECUPERAÇÃO
# Media acima de 7.0 ou superior APROVADO

nota1 = float(input('insira sua primeira nota: '))
nota2 = float(input('insira sua segunda nota: '))
media = (nota1 + nota2) / 2
if media <= 5.0:
    print('Media {}, REPROVADO'.format(media))
elif 5.1 <= media <= 6.9:
    print('Média {}, RECUPERAÇÃO'.format(media))
else:
    print('Media {}, APROVADO'.format(media))