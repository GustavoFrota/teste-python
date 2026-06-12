faturamento = float(input("Preencha com o faturamento (apenas números): ").replace(",", ".")); #input é usada para receber dados digitados pelo usuário pelo teclado
custo = 600;
lucro = faturamento - custo;
texto = f"O faturamento foi {faturamento}";

print(texto);
print(lucro);