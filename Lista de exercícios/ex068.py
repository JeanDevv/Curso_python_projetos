from random import randint
vitoria_user = 0
while True:
    print("=-" * 15)
    print("VAMOS JOGAR PAR OU ÍMPAR")
    print("=-" * 15)
    number_user = int(input("Diga um valor: "))
    computer = randint(0, 10)
    total = number_user + computer
    tipo = ' '
    while tipo not in "PI":
        tipo = str(input("Par ou Ímpar? [P/I]" )).strip().upper()[0]
    print(f"Você jogou {number_user} e o computador {computer} e o total foi {total}.", end=" ")
    print("DEU PAR" if total % 2 == 0 else "DEU ÍMPAR")
    if tipo == "P":
        if total % 2 == 0:#variável pra calcular se deu PAR a somar dos valores
            vitoria_user += 1
            print("Você VENCEU! :)")
        else:
            print("Você PERDEU...:(")
            break
    elif tipo == "I":#variável pra calcular se deu ÍMPAR a somar dos valores
        if total % 2 == 1:
            print("Você VENCEU! :)")
            vitoria_user += 1
        else:
            print("Você PERDEU.... :(")
            break
    print("Vamos jogar novamente...")
print(f"GAME OVER! Você venceu {vitoria_user} vezes")