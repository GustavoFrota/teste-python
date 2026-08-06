def calcular():
    saldo = float(input("Digite o seu saldo: R$"))

    Valor_50 = (saldo * 0.50)
    valor_20 = (saldo * 0.20)
    valor_15 = (saldo * 0.15)
    valor_10 = (saldo * 0.10)
    valor_5 = (saldo * 0.05)

    print("-" * 40)
    print(f"50% de {saldo} é: R${Valor_50:.2f}")

    print("-" * 40)
    print(f"20% de {saldo} é: R${valor_20:.2f}")

    print("-" * 40)
    print(f"15% de {saldo} é R${valor_15:.2f}")

    print("-" * 40)
    print(f"10% de {saldo} é R${valor_10:.2f}")

    print("-" * 40)
    print(f"5% de {saldo} é R${valor_5:.2f}")


calcular()
