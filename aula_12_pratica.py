name = str(input("Qual é seu nome?")).strip()
if name.upper() == "CARLOS":
    print("Que nome legal!")
elif name.upper() == "KEZIA" or name.upper() == "JEAN" or name.upper() == "SILVA":
    print("Seu nome e bem popular!")
elif name.upper() in "ANA CLÁUDIA JÉSSICA JULIANA":
    print("Belo nome você tem!")
else:
    print("Seu nome e bem normal.")
print("Tenha um bom dia, {}!".format(name))
