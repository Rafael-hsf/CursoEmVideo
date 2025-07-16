# FAÇA UM PROGRAMA QUE LEIA O SEXO DE UMA PESSOA, MAS SO ACEITE OS VALORES M OU F. CASO ESTEJA ERRADO, PEÇA A DIGITAÇÃO
# NOVAMENTE ATÉ TER UM VALOR CORRETO.

sexo = str(input('Digite seu sexo: [M/F] ')).upper()
while sexo != 'M' and sexo != 'F':
    print('Opção invalida. tente novamente.')
    sexo = str(input('Digite novamente seu sexo: [M/F] ')).upper()
print('OBRIGADO!')
print('-=-'*30)

#SOLUÇÃO DO GUANABARA

sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos, por favor informe seu sexo: ')).strip().upper()[0]
print('sexo {} registrado com sucesso!'.format(sexo))


