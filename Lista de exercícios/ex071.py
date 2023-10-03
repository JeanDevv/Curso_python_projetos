print("=" * 40)
print("{:^40}".format("BANCO CEV"))
print("=" * 40)
saque_user = int(input("Que valor você quer sacar? R$"))
total = saque_user
cedulas = 50
total_cedulas = 0
while True:
    if total >= cedulas:
        total -= cedulas
        total_cedulas += 1
    if total_cedulas % 2 == 0:
        print("Valor indisponível para sacar, tente novamente!")
        break
    else:
        if total_cedulas > 0:
            print(f"Total de {total_cedulas} cédulas de R${cedulas}")
        if cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 5
        total_cedulas = 0
        if total == 0:
            break
print("=" * 40)
print("Volte sempre ao BANCO CEV! Tenha um bom dia!")
