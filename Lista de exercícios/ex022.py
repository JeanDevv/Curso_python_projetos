'''Função ,strip() já vai eliminar os espaço caso o usúario colocar antes de dígitar'''
name = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(name.upper()))
print('Seu nome em minúsculas é {}'.format(name.lower()))
'''Ele vai mostrar o resultado da linha 1 com espaços. quando inserir o variavel.count(aspas) ele vai mostrar sem os espaços dado pelo usuario lá na linha 1'''
print('Seu nome tem ao todo {} letras'.format(len(name) - name.count(' ')))
'''O variavel.find('  ') faz com que ele conte quantas letras tem o primeiro nome digitado'''
#print('Seu primeiro nome tem {} letras'.format(name.find(' ')))
'''Nessa seção ele vai separar as letras dos nome digitado pelo usuario essa e a maneira que ocupa menos espaço'''
#print(name.split())
'''Maneira que ocupa mais espaço na memória'''
separador = name.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separador[0], len(separador[0])))