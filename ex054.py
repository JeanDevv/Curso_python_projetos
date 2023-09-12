from datetime import date
year_current = date.today().year
amounts_users = 0 #Aqui está criando uma variável de contador vazio atribuindo 0 a variável para utilizar como contador p/ + 
smaller_users = 0 #Aqui está criando uma variável pra utilizar como contador p/ -
for counter_year_users in range(1, 8):
    year_users = int(input("Em que ano a {}ª pessoa nasceu: ".format(counter_year_users)))
    age_users = year_current - year_users #Nessa variável está calculando a idade do usuário
    if  age_users >= 18: #Nesse campo do if está vendo se a idade dos usuários são maior que 20
        amounts_users += 1 #Está somando caso seja igual o maior que 18 e adicionando a um contador
    else:
        smaller_users += 1 #Está somando caso seja menor do que a idade 18
print("Ao todo tivemos {} pessoas maiores de idade!".format(amounts_users))
print("É também tivemos {} pessoas menores de idade".format(smaller_users))