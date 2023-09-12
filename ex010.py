real = float(input('Quanto você tem em dinheiro na sua carteira? R$'))
dolar = real / 2.25
euro = real / 2.40
print('Com a quantidade de R${:.2f} você conseguir comprar US${:.2f}'
      ' e também essa quantidade conseguir comprar euro que convertido é €{:.2f}'.format(real, dolar, euro))