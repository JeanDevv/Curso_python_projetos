while True:
    print("-" * 30)
    question_user = int(input("Quer ver a tabuada de valor? "))
    print("-" * 30)
    if question_user < 0:
        break
    for c in range(1, 11): #vai fazer a repetição de número de 1 até 10 na linha 10
        print(f'''{question_user} x {c} = {question_user*c}''')
print("PROGRAMA TABUADA ENCERRADO. Volte sempre!")