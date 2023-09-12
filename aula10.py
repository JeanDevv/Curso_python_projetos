'''Para o algoritmo identificar que e o mesmo nome em minusculo ou mausculo e só utilizar o upper()'''
'''nome = str(input('Qual é seu nome? ')).strip()
if nome.upper() == 'JEAN':
    print('Que nome legal você tem!')
else:
    print('Seu nome é esquisito!')
print('Bom dia, {}'.format(nome))'''
n1 = float(input('Digite a 1ª nota: '))
n2 = float(input('Digite a 2ª nota: '))
m = (n1 + n2)/2
print('Sua média foi {:.1f}'.format(m))
if m >=6.0:
    print('Sua média foi boa! Parabéns!')
else:
    print('Sua média foi ruim! Estude mais!')