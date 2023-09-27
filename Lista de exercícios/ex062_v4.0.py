print("-=" * 10)
print("Gerador de PA")
print("-=" * 10)
termo_user = int(input("Digite o termo: "))
razao_user = int(input("Qual a razão? "))
termo = termo_user
contador_user = 1 
more_termo = 10
total_termos = 0
while more_termo != 0:
    total_termos += more_termo
    while contador_user <= total_termos:
        print("{} -> ".format(termo), end="")
        termo += razao_user
        contador_user += 1
    print("PAUSA")
    more_termo = int(input("Quantos termos a mais deseja ver? "))
    total_termos += 0
print("Foram visualizados {} termos no total".format(total_termos))