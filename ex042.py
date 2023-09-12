print("-=" * 30)
print('Analisador de Triângulos')
print("-=" * 30)
reta_1 = float(input("Primeiro segmento: "))
reta_2 = float(input("Segundo segmento: "))
reta_3 = float(input("Terceiro segmento: "))
if reta_1 < reta_2 + reta_3 and reta_3 < reta_1 + reta_2:
    print("Os segmentos acima podem formar um triângulo ", end="")
    if reta_1 == reta_2 == reta_3:
        print("equilátero!")
    elif reta_1 != reta_2 != reta_3 != reta_1:
        print("escaleno!")
    else:
        print("isósceles!")
else:
    print("Os segmentos acima não podem formar um triângulo!")
print("-=" * 30)