num = int(input("Digite um número para ver a sua tabuada: ".strip()))
for c in range(1, 11):
    print(" {} x {} = {}".format(num, c, num*c))