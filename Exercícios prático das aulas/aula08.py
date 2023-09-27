#import math
from math import sqrt, floor, ceil
num = int(input('Digite um número:'))
#raiz = math.sqrt(num)
#print('A raiz de {} é igual a {}'.format(num, math.floor(raiz)))
raiz = sqrt(num)
print('A raiz de {} é igual a {}'.format(num, ceil(raiz)))
