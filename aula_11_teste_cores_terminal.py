'''print('\033[1;31;43mOlá, mundo!\033[m')'''

#Outro exemplo

'''a = 5
b = 10

print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m'.format(a, b))'''

#Outra maneira de formatar

nome = "Carlos"

cores = {"limpa": "\033[m", "azul":"\033[34m", "amarelo":"\033[33m", "preto_branco": "\033[7;30m"}

print('Muito prazer em te conhecer {}{}{}'.format(cores["amarelo"], nome, cores["limpa"]))