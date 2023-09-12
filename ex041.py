from datetime import date
year_current = date.today().year
date_birth_athlete = int(input("Ano de nascimento: ".strip()))
age_athlete = year_current - date_birth_athlete
print("O atleta tem {} anos.".format(age_athlete))
if age_athlete <= 9:
    print("Classificação: MIRIM")
elif age_athlete > 9 and age_athlete <= 14:
    print("Classificação: INFANTIL")
elif age_athlete > 14 and age_athlete <=19:
    print("Classificação: JÚNIOR")
elif age_athlete <= 25:
    print("Classificação: SÊNIOR")
else:
    print("Classificação: MASTER")
