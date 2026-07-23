capital = float(input("Digite o capital: "))

taxa = float(input("Digite a taxa: ")) / 100

periodo = int(input("Digite o período em meses: "))

montante = capital * (1 + taxa)**periodo

print(f"Montante final: R$ {montante:.2f}")