sex_person = str(input("Informe seu sexo: [Masculino/Feminino]: ")).upper().strip()[0]
while sex_person not in "MmFf":
    sex_person = str(input("Dado inválidos. Por favor, Digite novamente seu sexo: ")).upper().strip()[0]
print("Sexo {} registrado com sucesso".format(sex_person))