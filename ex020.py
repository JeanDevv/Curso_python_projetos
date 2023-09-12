from random import shuffle
pe1 = str(input('Primeiro aluno: '))
pe2 = str(input('Segundo alino: '))
pe3 = str(input('Terceiro aluno: '))
pe4 = str(input('Quarto aluno: '))
list = [pe1, pe2, pe3, pe4]
shuffle(list)
print('A ordem de apresentação será')
print(list)
#import random
#pe1 = str(input('Primeiro aluno: '))
#pe2 = str(input('Segundo alino: '))
#pe3 = str(input('Terceiro aluno: '))
#pe4 = str(input('Quarto aluno: '))
#list = [pe1, pe2, pe3, pe4]
#random.shuffle(list)
#print('A ordem de apresentação será')
#print(list)