from random import randint
from time import sleep

itens = ("PEDRA", "PAPEL", "TESOURA")
computer = randint(0, 2)

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

print("-=" * 15)
player = int(input("Qual é sua jogada?".strip()))
print("JO")
sleep(0.5)
print("KEN")
sleep(0.5)
print("PÔ")
sleep(0.5)
print("O computador escolheu {}".format(itens[computer]))
print("Você escolheu {}".format(itens[player]))
print("=-" * 15)

color_palette = {"red": "\033[31m", "end_color": "\033[m"} #PALETA DE CORES

if computer == player == 0:
    print("EMPATE")
elif (computer == 0 and player == 2) or (computer == 1 and player == 0) or (computer == 2 and player == 1):
    print("Computador ganhou!")
elif (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
    print("Você ganhou!")
else:
    print("{}Opção inválida{}".format(color_palette["red"], color_palette["end_color"]))
