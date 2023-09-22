number_user = 0
question_user = "S"
maior_valor = 0
menor_valor = 0
quantidade_numbers = 0
media_valores = 0
soma_valores = 0
while question_user == "S":
    number_user = int(input("Digite um valor: "))
    question_user = str(input("Deseja continuar[S/N]? ")).strip().upper()[0]
    quantidade_numbers += 1
    soma_valores += number_user
    if quantidade_numbers == 1:
        maior_valor = menor_valor = number_user
    else:
        if number_user > maior_valor:
            maior_valor = number_user
        if number_user < menor_valor:
            menor_valor = number_user
media_valores = number_user / quantidade_numbers
print("A quantidade de valores digitados foram {} e a média da soma entre eles é {}".format(quantidade_numbers, media_valores))
print("O maior valor digitado foi {} e o menor {}".format(maior_valor, menor_valor))
