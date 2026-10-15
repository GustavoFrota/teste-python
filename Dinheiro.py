from time import sleep

def calcular():
    while True:
        try:
            saldo = float(input("Digite o seu saldo: "))
            break
        except ValueError:
            print("ERRO! Digite apenas números")
    print('CALCULANDO RENDA...')
    sleep(3)

    porcentagens = [50, 20, 10, 10, 10]
    distribuicoes = ['Gastos essenciais', 'Sonho de consumo', 'Gastos não essenciais', 'Reserva', 'Investimento']

    print('=' * 40)

    print("RENDA ORGANIZADA")

    for porcentagem, distribuicao in zip(porcentagens, distribuicoes):
          valor = saldo * porcentagem / 100

          print('=' * 40)
          print(distribuicao)
          print(f"{porcentagem}% de R${saldo:.2f} --> R${valor:.2f}")

calcular()