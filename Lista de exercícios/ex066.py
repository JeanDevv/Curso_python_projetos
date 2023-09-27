quantidade_number = soma_valores = 0
while True:
    number_user = int(input("Digite um valor [999 para parar]: "))
    if number_user == 999:
        break
    quantidade_number += 1
    soma_valores += number_user
print(f"A soma dos {quantidade_number} valores foi {soma_valores}!")