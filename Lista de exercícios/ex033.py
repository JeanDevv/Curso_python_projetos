num_valor_1 = int(input('Primeiro valor: '))
num_valor_2 = int(input('Segundo valor: '))
num_valor_3 = int(input('Terceiro valor: '))

menor = num_valor_1 
if num_valor_2 < num_valor_1 and num_valor_2 < num_valor_3:
    menor = num_valor_2
if num_valor_3 < num_valor_1 and num_valor_3 < num_valor_2:
    menor = num_valor_3

maior = num_valor_1
if num_valor_2 > num_valor_1 and num_valor_2 > num_valor_3:
    maior = num_valor_2
if num_valor_3 > num_valor_1 and num_valor_3 > num_valor_2:
    maior = num_valor_3

print("O menor valor digitado foi {}".format(menor))
print("O maior valor digitado foi {}".format(maior))
