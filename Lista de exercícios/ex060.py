#Metodo de calcular fatorial com a biblioteca que há dentro do python
#from math import factorial
#number_factorial = int(input("Digite um número para calcular o seu Fatorial: "))
#factorial_for_number = factorial(number_factorial)
#print("O fatorial de {} é {}".format(number_factorial, factorial_for_number))
#Metodo de calcular da maneira sem a biblioteca p/ caso que ocorra em outras linguagens
number_user = int(input("Digite um número para calcular o Fatorial: "))
contador = number_user
fatorial = 1
print("Calculando {}! = ".format(number_user), end="")
while contador > 0:
    print("{}".format(contador), end="")
    #print(" x " if contador > 1 else " =", end="") #maneira simplificada
    if contador > 1:
        print(" x ", end="")
    else:
        print(" =", end="")
    fatorial *= contador
    contador -= 1
print(" {}".format(fatorial))
