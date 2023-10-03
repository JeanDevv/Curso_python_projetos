total_pessoas = pessoas_com_18_anos = total_homens = total_mulheres_menos_20_anos = 0
while True: 
    print("-" * 22)
    print(" CADASTRE UMA PESSOA ")
    print("-" * 22)
    idade = int(input("Idade: "))
    sexo = ' '
    while sexo not in "MF":
        sexo = str(input("Sexo: [M/F] ")).strip().upper()[0]
    if idade == 18:
        pessoas_com_18_anos += 1
    if sexo == "M":
        total_homens += 1
    if sexo == "F" and idade <= 20:
        total_mulheres_menos_20_anos += 1
    print("-" * 22)
    question = " "
    while question not in "SN":
        question = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    print("-" * 22)
    if question == "N":
        break
print(f'''Total de pessoas com mais de 18 anos: {pessoas_com_18_anos}
Ao todo temos {total_homens} homens cadastrados
E temos {total_mulheres_menos_20_anos} com menos de 20 anos''')