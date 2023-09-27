'''esse exercicio para verificar se tem uma palavra no nome onde o usuário digitou
o .strip() e para tirar os espaços e o .upper() e para o algoritmo entender que o
o usuário pode digitar em maiusculo ou minusculo'''
city = str(input('Em que cidade você nasceu? ')).strip()
print(city[:5].upper() == "SANTO")
