'''year = int(input('Que ano quer analisar? coloque 0 para analisar o ano atual: '))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('O ano {} é bissexto'.format(year))
else:
    print('O ano {} não é bissexto'.format(year))'''

#Verificação de ano bissexto que também analisa o ano atual

from datetime import date
year = int(input('Que ano quer analisar? coloque 0 para analisar o ano atual: '))
if year == 0:
    year = date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('O ano {} é bissexto'.format(year))
else:
    print('O ano {} não é bissexto'.format(year))