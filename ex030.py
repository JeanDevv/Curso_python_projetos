number = int(input('Digite o primeiro número qualquer: '.strip()))
result = number % 2
if result == 0: #quando o resultado for 0 o nº digitado e par e quando for 1 e ímpar
    print('O número {} é PAR'.format(number))
else:
    print('O número {} é ÍMPAR'.format(number))