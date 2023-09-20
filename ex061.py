print("Gerador de PA")
print("-=" * 10)
primeiro_termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
termo = primeiro_termo
contador = 1
while contador <= 10:
    print("{} → ".format(termo), end="")
    termo += razao
    contador += 1 
print("Fim")