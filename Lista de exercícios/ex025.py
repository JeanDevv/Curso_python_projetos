#Nesse exercicio aprendenrá a verificar se tem no nome a palavra que busca, como exercicio anterior utiliza-se o upper()
'''nome = str(input('Qual é seu nome completo?')).strip()
print('Seu nome tem Silva? {}'.format(nome[:5].upper() == 'SILVA'))'''
#Essa maneira você utilizada a função in "variável" ele vai identificar no nome inteiro se tem "Silva"
nome = str(input('Qual é seu nome completo?')).strip()
print('Seu nome tem Silva? {}'.format("SILVA" in nome.upper()))
