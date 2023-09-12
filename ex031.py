viagem = float(input('Qual é a distância da viagem? '.strip()))
print('Você está prestes a começar uma viagem de {}km.'.format(viagem))
'''if viagem <= 200:
    preço = viagem * 0.50
else:
    preço = viagem * 0.45'''
preço = viagem * 0.50 if viagem <= 200 else viagem * 0.45
print('É o preço da sua passagem será de R${:.2f}'.format(preço))