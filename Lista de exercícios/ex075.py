number = (int(input("Digite um número: ")), 
int(input("Digite outro número: ")),
int(input("Digite mais um número: ")), 
int(input("Digite o último número: ")))
print(f"Você digitou os valores {number}")
if 9 in number:
    print(f"O valor 9 apareceu {number.count(9)} vez") #função count vai contar quantas vezes apareceu certo elemento na variável
else:
    print("O valor 9 não apareceu em nenhuma das posições!")
if 3 in number:
    print(f"O valor 3 apareceu na {number.index(3)+1}ª posição") #função index busca a posição do elemento que deseja
else:
    print("O valor 3 não foi digitado em nenhuma posição!")
print("Os números pares digitados foram: ", end="")
for repent_number in number:
    if repent_number % 2 == 0:
        print(repent_number, end=" ")