weight_client = float(input("Qual é seu peso? ".strip()))
height_client = float(input("Qual é sua altura? ".strip()))
imc = weight_client / (height_client ** 2) 
print("O seu IMC é {:.1f}".format(imc))
if imc <= 18.5:
    print("Abaixo do peso")
elif imc > 18.5 and imc <= 25:
    print("Peso ideal")
elif imc > 25 and imc <= 30:
    print("Sobrepeso")
elif imc > 30 and imc <= 40:
    print("Obesidade")
else:
    print("Obesidade mórbida")