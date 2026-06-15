faturamento = int(input("Digite o faturamento: "))
custo = int(input("Digite o custo: "))

lucro = faturamento - custo

if lucro >= 0:
    print("lucro de", lucro)
    print("Deu lucro")
else:
    print("prejuízo de", lucro)
    print("Deu prejuízo")