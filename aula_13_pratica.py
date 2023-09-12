#1º EXEMPLO
#for c in range(1, 6): #SEMPRE O ÚLTIMO NÚMERO E IGNORADO
#    print("OI") #NESSE CASO ELE EXECUTARÁ SOMENTE DE 1 ATÉ 5 A PALAVRA "OI"
#print("FIM")

#2º EXEMPLO
#for c in range(6, 0, -1): #NESSE EXEMPLO ELE FARÁ A CONTAGEM DE 0 ATÉ 6 SÓ QUE DE TRÁS PARA FRENTE 
#    print(c)
#print("FIM")

#3º EXEMPLO
#for c in range(0, 7, 2): #NESSE EXEMPLO ELE CONTOU PULANDO DE 2 EM 2 NÚMEROS
#    print(c)
#print("FIM")

#4º EXEMPLO
#n = int(input("Digite um número: "))
#for c in range(0, n+1):
#    print(c)
#print("FIM")

#5º EXEMPLO
#inicio = int(input("Início: ".strip()))
#fim = int(input("Fim: ".strip()))
#passo = int(input("Passo: ".strip())) #essa variável vai indicar a quantidade de número que deve pular
#for c in range(inicio, fim+1, passo):
#    print(c)
#print("FIM")

#6º EXEMPLO
#for c in range(0, 3):
#    numero = int(input("Digite um número: ".strip()))
#print("FIM")

#7º EXEMPLO
soma = 0
for c in range(0, 4):
    numero = int(input("Digite um número: ".strip()))
    soma += numero
print("O somatório de todos os valores foi {}".format(soma))