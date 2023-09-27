sum_ages = 0
medium_age = 0
amount_age_man = 0
name_man_old = 0
current_age_small_age_woman = 0
for group_person in range(1, 5):
    print("--------- {} ª PESSOA ---------".format(group_person))
    names = str(input("Nome: ")).strip()
    ages = int(input("Idade: "))
    sexes = str(input("Sexo [M/F]: ")).strip()
    sum_ages += ages
    if group_person == 1 and sexes in "Mm":
        amount_age_man = ages
        name_man_old = names
    if sexes in "Mm" and ages > amount_age_man:
        amount_age_man = ages
        name_man_old = names
    if sexes in "Ff" and ages < 20:
        current_age_small_age_woman += 1
medium_age = sum_ages / 4
print("A média de idade do grupo é de {} anos".format(medium_age))
print("O homem mais velho tem {} anos e se chama {}".format(amount_age_man, name_man_old))
print("Ao todo são {} mulheres com menos de 20 anos".format(current_age_small_age_woman))