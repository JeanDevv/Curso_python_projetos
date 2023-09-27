print("-=" * 30)
print("Olá seja bem-vindo ao espaço de Empréstimo!")
resposta_do_cliente = str(input("Gostaria de fazer uma simulação de empréstimo? ".strip()))
if resposta_do_cliente.upper() == "SIM":
    valor_da_casa = float(input("Qual e o valor da casa? R$ ".strip()))
    salário_client = float(input("Valor da renda mensal? R$ ".strip()))
    tempo_do_financiamento = int(input("Quantos anos de financiamento? ".strip()))
    valor_parcela_mensal = valor_da_casa / (tempo_do_financiamento * 12)
    minimo_da_parcela = salário_client * 30 / 100
    print("Para financiar uma casa no valor de {:.2f} em {} anos, ".format(valor_da_casa, tempo_do_financiamento), end="")
    print("o valor da parcela mensal será de R${:.2f}".format(valor_parcela_mensal))
    cores_das_letras = {"green": "\033[32m", "red": "\033[31m", "fim_da_fonte": "\033[m"}
    if valor_parcela_mensal <= minimo_da_parcela:
        print("Empréstimo foi {}aprovado!{}".format(cores_das_letras["green"], cores_das_letras["fim_da_fonte"]))
    elif valor_parcela_mensal >= minimo_da_parcela:
        print("Empéstimo {}negado!{}".format(cores_das_letras["red"], cores_das_letras["fim_da_fonte"]))
elif resposta_do_cliente.upper() == "NÃO":
    print("Volte sempre!")
