def calcular():
    while True:
        try:
            saldo = float(input("Digite o seu saldo: "))
            break
        except ValueError:
            print("ERRO! Digite apenas números")

    porcentagens = [50, 20, 15, 10, 5]
    print('-' * 40)

    print("ORGANIZANDO RENDA")

    for porcentagem in porcentagens:
        valor = saldo * porcentagem / 100

        print('-' * 40)
        print(f"{porcentagem}% de R${saldo:.2f} é R${valor:.2f}")

calcular()