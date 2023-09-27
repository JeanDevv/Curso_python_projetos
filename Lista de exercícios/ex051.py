print("=" * 30)
primeiro_numero = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
decimo = primeiro_numero + (10 - 1) * razao
for c in range(primeiro_numero, decimo + razao, razao):
    print("{} ".format(c), end="→ ")
print("ACABOU")
