faturamento = int(input("Digite o faturamento: "))
custo = int(input("Digite o custo: "))

lucro = faturamento - custo

if lucro >= 0:
    print("lucro de", lucro)
    print("Deu lucro")
else:
    print("prejuízo de", lucro)
    print("Deu prejuízo")

produtos = ['iphone', 'ipad', 'airpod']
novo_produto = input("Digite o nome do produto: ")

if novo_produto in produtos:
    print("produto já existente")
else:
    print(f"{novo_produto} cadastrado com sucesso")
    produtos.append(novo_produto)

print(produtos)

vendas = 20000

if vendas >= 15000:
    bonus = 500
elif vendas >= 5000:
    bonus = 100
else:
    bonus = 0

print(f"O bônus do funcionário foi de {bonus}")