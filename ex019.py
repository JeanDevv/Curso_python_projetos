#import random
#pe1 = str(input('Primeiro aluno: '))
#pe2 = str(input('Segundo aluno: '))
#pe3 = str(input('Terceiro aluno: '))
#pe4 = str(input('Quarto aluno: '))
#list = [pe1, pe2, pe3, pe4]
#random = random.choice(list)
#print('O aluno escolheido foi {}'.format(random))
from random import choice
pe1 = str(input('Primeiro aluno: '))
pe2 = str(input('Segundo aluno: '))
pe3 = str(input('Terceiro aluno: '))
pe4 = str(input('Quarto aluno: '))
list = [pe1, pe2, pe3, pe4]
random = choice(list)
print('O aluno escolheido foi {}'.format(random))
