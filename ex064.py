number_user = 0#está vazio o variável para que quando o user digitar um valor ele se torna o valor da variável
contador = 0 #essa variavel vai contar tudo que for digitado pelo user
soma = 0#essa variável vai ser utilizado para somar dentro do while
number_user = int(input("Digite um número: "))
while number_user != 999:# "!=" significa diferente ou igual
    number_user = int(input("Digite um número: "))#A variável está sendo repetido porque vai ser desconsiderado o valor digitado 999 e o print da linha 9 vai somar somente o que foi digitado e somado o que está fora do while
    soma += number_user #está utilizando a variável vazia para somar os todos os números digitados pelo user menos o 999
    contador += 1#Aqui ele vai dizer quantas vezes digitaram número antes de digitarem o número 999
print("O total de números digitados foram {} e a soma entre eles e {}".format(contador, soma))