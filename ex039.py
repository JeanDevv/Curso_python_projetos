from datetime import date 
ano_atual = date.today().year
data_candidato = int(input("Qual e seu ano de nascimento: ".strip())) #data de nascimento do candidato
idade_candidato = ano_atual - data_candidato # nessa linha está calculando p/ saber quantos anos o candidato tem
print("Você tem {} anos em {}".format(idade_candidato, ano_atual))
if idade_candidato == 18:
    print("Você deve se apresentar logo ao posto militar para se alistar!")
elif idade_candidato < 18:
    falta_alistamento = 18 - idade_candidato #Essa variável vai calcular quantos anos falta pro candidato se alistar
    print("Você não possui a idade mínima para se alistar ainda, falta {} anos para poder se alistar".format(falta_alistamento))
elif idade_candidato > 18:
    ano_de_alistamento1 = (ano_atual - data_candidato) - 18 # essa variável vai calcular e dar a resposta de quanto anos atrás o candidato deveria ter se candidatado
    ano_de_alistamento2 = ano_atual - ano_de_alistamento1 # essa variável vai pegar a variável acima e calcular e dar o ano que deveria ter se alistado
    print("Você deveria ter se alistado a {} atrás no ano de {}.".format(ano_de_alistamento1, ano_de_alistamento2))
else:
    print("Opção inválida")
