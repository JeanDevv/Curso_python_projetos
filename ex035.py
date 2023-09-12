print("-=" * 20)
print('Analisador de Triângulos')
print("-=" * 20)

reta_1 = float(input("Primeiro segmento: "))
reta_2 = float(input("Segundo segmento: "))
reta_3 = float(input("Terceiro segmento: "))

if reta_1 < reta_2 + reta_3 and reta_3 < reta_1 + reta_2:
    print("Os segmentos acima podem formar um triângulo!")
else:
    print("Os segmentos acima não podem formar um triângulo!")