salario_funcionario = float(input("Qual e o salário do funcionário? "))
if salario_funcionario <= 1250:
    novo_salario = salario_funcionario + (salario_funcionario * 15 / 100)
else:
    novo_salario = salario_funcionario + (salario_funcionario * 10 / 100)
print("Quem ganhava R${:.2f} passará a ganhar R${:.2f} agora".format(salario_funcionario, novo_salario))