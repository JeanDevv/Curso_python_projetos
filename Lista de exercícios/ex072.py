cont = ("zero", "um", "dois", "três", "quatro", "cinco",
"seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze",
"catorze", "quinze", "dizesseis", "dizessete", "dezoito",
"dezenove", "vinte")
while True:
    num = int(input("Digite um número: "))
    if 0 <= num <= 20:
        break
    question = " "
    print("Tente novamente. ", end="")
    print(f"Você digitou o número {cont[num]}")
