print("{:-^40}".format(" LOJA SUPER BARATÃO "))
total_compras = quantidade_produtos_mais_caro = quantidade_produtos = menor_produto = 0
produto_barato = " "
while True:
    nome_produto = str(input("Nome do produto: ")).strip()
    valor_produto = float(input("Preço: "))
    quantidade_produtos += 1
    total_compras += valor_produto
    if valor_produto >= 1000:
        quantidade_produtos_mais_caro += 1
#    if quantidade_produtos == 1 or valor_produto < menor_produto:
        menor_produto = valor_produto
        produto_barato = nome_produto
    else:
        if valor_produto < menor_produto:
            menor_produto = valor_produto
            produto_barato = nome_produto
    question = " "
    while question not in "SN":
        question = str(input("Quer continuar? ")).strip().upper()[0]
    if question == "N":
        break
print("{:-^40}".format(" FIM DO PROGRAMA "))
print(f"O total de compra foi {total_compras}")
print(f"Temos {quantidade_produtos_mais_caro} produtos custando mais de R$1.000,00")
print(f"O produto mais barato foi {produto_barato} que custa R$ {menor_produto}")