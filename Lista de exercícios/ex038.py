primeiro_numero = int(input("Digite o primeiro número: ".strip()))
segundo_numero = int(input("Digite o segundo número: ".strip()))
if primeiro_numero > segundo_numero:
    print("O primeiro número e maior!")
elif segundo_numero > primeiro_numero:
    print("O segundo número e maior!")
#MANEIRA DE UMA FUNÇÃO SABER SE = AS VARIAVEIS
#elif segundo_numero == primeiro_numero:
     #print("Os dois números digitados são iguais!")'''
#MANEIRA SIMPLIFICADA PARA SABER SE AS VARIAVEIS SÃO =
else:
    print("Os valores digitados são iguais!")
