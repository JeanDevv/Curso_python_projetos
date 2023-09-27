print("-" * 30)
print("Sequência Fibionacci")
print("-" * 30)
termo_user = int(input("Quantos termos deseja ver: "))
print("~" * 30)
contador = 3 
termo_1 = 0
termo_2 = 1
print("{} -> {}".format(termo_1, termo_2), end="")
while contador <= termo_user:
    termo_3 = termo_1 + termo_2
    print(" -> {}".format(termo_3), end="")
    termo_1 = termo_2
    termo_2 = termo_3
    contador += 1
print(" -> Fim")
print("~" * 30)