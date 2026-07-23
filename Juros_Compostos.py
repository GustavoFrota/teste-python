c = float(input("Digite o capital: "))

i = float(input("Digite a taxa: "))

taxa = i / 100

n = int(input("Digite o período: "))

montante = c * (1 + taxa)**n

print(montante)