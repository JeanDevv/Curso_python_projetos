frase = str(input("Digite uma frase: ")).strip().upper()
divisao_palavra = frase.split() #função split() faz a separação das palavras digitadas
frase_espaco = "".join(divisao_palavra) #Função .join(variável) faz com que e removida o espaço da variável
#frase_invertida_simplificada = frase_espaco[::-1]
frase_invertida = ""
for letra in range(len(frase_espaco) -1, -1, -1):
    frase_invertida += frase_espaco[letra]
print('O inverso de {} e {}'.format(frase_espaco, frase_invertida))
if frase_invertida == frase_espaco: 
    print("Temos um palíndromo!")
else:
    print("A frase não é um palíndromo!")