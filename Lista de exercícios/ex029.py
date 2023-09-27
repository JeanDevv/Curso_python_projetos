km = float(input('Qual é a velocidade atual do carro? '.strip()))
if km > 80:
    print('MULTADO! Você atingiu o limite da via que é de 80km/h')
    multa = (km-80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
else:
    print('Tenha um bom dia, dirija com cuidado!')
