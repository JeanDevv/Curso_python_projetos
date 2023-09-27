n = int(input('Digite um número:'))
print('O dobro de {} é {}'.format(n, (n * 2)))
#print('é o triplo de {} vale {}, é a raiz quadrada de {} é {:.1f}'.format(n, (n * 3), n, (n ** (1 / 2))))
print('é o triplo de {} vale {}. \né a raiz quadrada de {} é {:.2f}'.format(n, (n * 3), n, pow (n, (1 / 2))))