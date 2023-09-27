amounts_person = 0
smaller_person = 0 
for weight in range(1, 6):
    weight_person = float(input("Peso da {}ª pessoa: ".format(weight)))
    if weight == 1:
        amounts_person = weight_person #nessa variável ele está pegando o maior valor informado pelo usuário e ele definir como maior peso
        smaller_person = weight_person #nessa variável ele está pegando o menor valor informado pelo usuário e ele definir como menor peso
    else:
        if weight_person > amounts_person: #Nessa linha ele está verificando se a variável informado pelo usuário foi maior que o peso definido no if weight
            amounts_person = weight_person #Caso seja maior ele vai redefinir o maior peso novamente
        if weight_person < smaller_person: #Nessa linha ele está fazendo a mesma verificação, porém está verificando o valor informado pelo usuário e menor do que definido no if de weight
            smaller_person = weight_person #Caso seja menor ele vai redefinir para o menor peso informado novamente
print("O maior peso lido foi {}Kg".format(amounts_person))
print("O menor peso lido foi {}Kg".format(smaller_person))