print("Gerador de PA")
print("-=" * 15)
primeiro_termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
termo = primeiro_termo
contador = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while contador <= total:
        print("{} → ".format(termo), end="")
        termo += razao
        contador += 1
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar a mais? "))
print("Progressão finalizada com {} termos mostrados".format(total))