from random import randint
from time import sleep #biblioteca para importar tempo
pc = randint(0, 5) #FAZ A MAQUINA CHUTAR UM Nº
print('-=-' * 18)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 18)
user = int(input('Em que número eu pensei? ')) #USER TENTA ADIVINHAR O Nº
print('PROCESSANDO....')
sleep(0.5)
if user == pc:
    print('Parabéns você acertou o nº!!')
else:
    print('Errou!! eu pensei no nº {} e não no {}!'.format(pc, user))
