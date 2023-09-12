print("{:=^40}".format(" LOJA CARLOS "))
price_product = float(input("Preço das compras: R$".strip()))
print('''FORMAS DE PAGMENTOS
[ 1 ] À vista 
[ 2 ] Cartão de débito
[ 3 ] 2x Cartão de crédito
[ 4 ] 3x ou mais no cartão de crédito''')
options = int(input("Qual é a opção? ".strip()))
if options == 1:
    total  = price_product - (price_product * 10 / 100)
elif options == 2:
    total = price_product - (price_product * 5 / 100)
elif options == 3:
    total = price_product
    portion = total / 2
    print("Seu produto ficará de 2x de R${:.2f} SEM JUROS".format(portion))
elif options == 4:
    total = price_product + (price_product * 20 / 100)
    amount_portion = int(input("De quantas vezes deseja parcelar sua compra? ".strip()))
    
    total_portion = total / amount_portion
    print("Sua compra será parcelada em {}x de R${:.2f} COM JUROS".format(amount_portion, total_portion))
else:
    total = price_product
    color_palette = {"red": "\033[31m", "end_color": "\033[m"}
print("{}Opção inválida, tente novamente!{}".format(color_palette["red"], color_palette["end_color"]))
print("Sua compra e no valor de R${:.2f} com o desconto passa a ser R${:.2f} na hora de finalizar a compra.".format(price_product, total))