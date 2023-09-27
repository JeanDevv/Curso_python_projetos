question_user = "S"
#quantidade__numbers = media_valores = soma_valores = media_valores = media_valores = 0 maneira simplificada de atribuir o mesmo valor p/ as variável
quantidade__numbers = 0
media_valores = 0
soma_valores = 0
maior_valor = 0
menor_valor = 0
while question_user in "Ss":
    number_user = int(input("Digite um número: "))
    soma_valores += number_user
    quantidade__numbers += 1
    if quantidade__numbers == 1:
        #maior_valor = menor_valor = number_user maneira de simplificar
        maior_valor = number_user
        menor_valor = number_user
    else:
        if number_user > maior_valor:
            maior_valor = number_user
        if number_user < menor_valor:
            menor_valor = number_user
    question_user = str(input("Quer continuar? [SIM/NÃO]")).upper().strip()[0]
media_valores = soma_valores / quantidade__numbers
print("Foram digitados {} e a média de todos os valores digitado é {}".format(quantidade__numbers, media_valores))
print("O maior número foi {} e o menor foi {}".format(maior_valor, menor_valor))