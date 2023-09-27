from time import sleep
first_number = int(input("Digite um número: "))
second_number = int(input("Digite mais um número: "))
option = 0
while option != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    option = int(input("Qual é sua opção? "))
    if option == 1:
        sum_numbers = first_number + second_number
        print("A soma de {} + {} = {}".format(first_number,second_number, sum_numbers))
    elif option == 2:
        multiplication = first_number * second_number
        print("A multiplicação entre {} x {} = {}".format(first_number, second_number, multiplication))
    elif option == 3:
        if first_number > second_number:
            bigger = first_number
        else :
            bigger = second_number
        print("O maior valor informado entre {} e {} e {}".format(first_number, second_number, bigger))
    elif option == 4:
        print("Informe novos números:")
        first_number = int(input("Digite 1ª número novo: "))
        second_number = int(input("Digite 2º número novo: "))
    elif option == 5:
        print("Finalizando...")
    else:
        print("Opção inválida. Tente novamente!")
sleep(1.5)
print("Fim do programa...Volte sempre!")