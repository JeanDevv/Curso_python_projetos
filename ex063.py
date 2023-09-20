print("-" * 30)
print("Sequência de Fibionacci")
print("-" * 30)
termo_user = int(input("Quantos termos você quer mostrar? "))
contador = 3
termo_1 = 0
termo_2 = 1
print("~" * 30)
print("{} -> {}".format(termo_1, termo_2), end="")
while contador <= termo_user:
    termo_3 = termo_1 + termo_2
    print(" -> {}".format(termo_3), end="")
    termo_1 = termo_2
    termo_2 = termo_3
    contador += 1
print(" -> FIM")
print("~" * 30)