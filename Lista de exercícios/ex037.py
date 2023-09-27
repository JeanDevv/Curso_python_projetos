numero = int(input("Digite um número inteiro: ".strip()))
print('''Escolha uma da bases para conversão:
[ 1 ] Converter para Binário
[ 2 ] Converter para Octal
[ 3 ] Converter para Hexadecimal''')

opcao_do_usuario = int(input("Qual opção você deseja: ".strip()))
if opcao_do_usuario == 1:
    print("{} convertido para Binário é igual a {}".format(numero, bin(numero)[2:]))
elif opcao_do_usuario == 2:
    print("{} convertido para Octal é igual a {}".format(numero, oct(numero)[2:]))
elif opcao_do_usuario == 3:
    print("{} convertido para Hexadecima é igual a {}".format(numero, hex(numero)[2:]))
else:
    print("Opção invalida")
     
