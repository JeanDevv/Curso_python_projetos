'''num = int(input('Informe um número: '))
n = str(num)
print('Analisando o número {}'.format(num))
print('Unidade : {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))'''
'''Função aonde você divide cada número separadamente por unidade, dezena, centena e milhar'''
num = int(input('Informe um número: '))
unid = num // 1 % 10
cent = num // 10 % 10
dez = num  // 100 % 10
mil = num  // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade : {}'.format(unid))
print('Dezena: {}'.format(dez))
print('Centena: {}'.format(cent))
print('Milhar: {}'.format(mil))
