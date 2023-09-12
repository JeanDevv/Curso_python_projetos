from random import randint #aqui está importando a biblioteca random, porém está importando somente o módulo randint(modo que a máquina começa a chutar numeros aleatório que e definido pela pessoa que o programou)
computer = randint(0, 10)#nessa linha está determinado que a variável computer só poderá mostrar na tela número que estejam entre 0 a 10
print("Sou seu computador...Acabei de pensar em um número entre 0 e 10.")
print("Será que você consegue adivinhar qual foi?")
acertou = False #Essa Variável está com false(falso) para que enquanto não acertar o número ele vai continuar false
palpite = 0
while not acertou:
    player = int(input("Qual é o seu palpite? "))
    palpite += 1 #Aqui ele está acumulando quantas vezes o usuário deu o palpite
    if player == computer:
        acertou = True #Caso o usuário acerte o palpite a variável acertou fora da estrutura automaticamente se torna True(verdadeiro)
    else:
        if player < computer:#esse if vai ver se o número informado pelo usuário e menor que o número que o computador pensou
            print("Mais...Tente mais uma vez!")
        if player > computer: #esse if e pra ver se o usuário passou do número que o computador pensou
            print("Menos...Tente novamente!")
print("Acertou com {} tentativa. Parabéns!".format(palpite))
