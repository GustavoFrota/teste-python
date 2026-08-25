def calcular():
    while True:
        try:
            saldo = float(input("Digite o seu saldo: "))
            break
        except ValueError:
            print("ERRO! Digite apenas números")

    porcentagens = [50, 20, 15, 10, 5]
    distribuicoes = ['Gastos essenciais', 'Sonho de consumo', 'Gastos não essenciais', 'Reserva', 'Investimento']

    print('=' * 40)

    print("ORGANIZANDO RENDA")

    for porcentagem, distribuicao in zip(porcentagens, distribuicoes):
          valor = saldo * porcentagem / 100

          print('=' * 40)
          print(distribuicao)
          print(f"{porcentagem}% de R${saldo:.2f} --> R${valor:.2f}")

calcular()