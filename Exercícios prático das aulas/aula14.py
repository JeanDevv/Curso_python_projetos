'''1ª exemplo
c = 1 
while c < 11:
    print(c)
    c += 1
print("FIM")

2ª exemplo

n = 1
while n != 0:
    n = int(input("Digite um valor: "))
print("FIM")

#3ª exemplo
r = "SIM"
while r == "SIM":
    n = int(input("Digite um valor: "))
    r = str(input("Quer continuar? [Sim/Não] ")).upper()
print("Fim")'''

#4º exemplo

n = 1
par = 0
impar = 0
'''par = impar = 0''' #maneira alternativa para criar variável com valor vazio
while n != 0:
    n = int(input("Digite um valor: "))
    if n!= 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print("Você digitou {} números pares e {} ímpares!".format(par, impar))