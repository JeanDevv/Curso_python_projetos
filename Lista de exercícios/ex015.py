dias = int(input('Quantos dias foram alugado o carro?'))
km = float(input('Quantos Km foram rodados?'))
pg = (dias * 60) + (km * 0.15)
print('O total a pagar do aluguel do carro é {:.2f}'.format(pg))
