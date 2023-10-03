#lanche = ("Hambúrger", "Suco", "Pizza", "Pudim", "Batata frita") pode fazer a estrutura de tupla sem parenteses agora na nova versão do python 3
#print(len(lanche))

#Maneira utilizando a função range() p/ saber a posição de cada elemento
#for cont in range(0, len(lanche)):
    #print(f"Eu vou comer {lanche[cont]} na posição {cont}")

#maneira onde você mostra a posição sem utilizar a função range()
#for posição, comida in enumerate(lanche):
#    print(f"Eu vou comer {comida} na posição {posição}")

#maneira simples
#for comida in lanche:
#    print(f"Eu vou comer {comida}")
#print("Comi pra caramba!!")

#Maneira de elementos reorganizado por nome
#print(sorted(lanche))
#print(lanche)

#Nesse exemplo ele está juntando duas tuplas, não somando os seus elementos!
#a = (2, 5, 4)
#b = (5, 8, 1, 2)
#c = a + b
#print(c)

#Nesse exemplo ele está contado quantos elementos tem nas duas tuplas
#a = (2, 5, 4)
#b = (5, 8, 1, 2)
#c = a + b
#print(len(c))

#nesse exemplo ele vai contar quantos vezes o número dentro do parentêse aparece em cada tupla
#a = (2, 5, 4)
#b = (5, 8, 1, 2)
#c = a + b
#print(c.count(5))

#Nesse exemplo ele vai mostrar em qual posição está o elemento que está dentro do parentese
#a = (2, 5, 4)
#b = (5, 8, 1, 2)
#c = b + a
#print(c.index(4))

#Exemplo caso tenha números repetidos
#a = (2, 5, 4)
#b = (5, 8, 1, 2)
#c = b + a
#print(c.index(5, 1)) #ele que buscar o 5 dentro dos elementos das tuplas, porém ele vai começar da posição um ignorando a posição 0 que é o 5

#Exemplo que pode misturar diferente tipos pode se colocar letras e números dentro das mesma tupla, só funciona somente no Python
#pessoa = ("Jean", 19, "Masculino", 60.0)
#print(pessoa)

#Exemplo de apagar uma tupla
pessoa = ("Jean", 19, "Masculino", 60.0)
del(pessoa)
print(pessoa)
