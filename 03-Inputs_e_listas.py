faturamento = input("Preencha com o faturamento (apenas números): "); #input é usada para receber dados digitados pelo usuário pelo teclado
faturamento = float(faturamento);
custo = 600;
lucro = faturamento - custo;
texto = f"O faturamento foi {faturamento}";

print(texto);
print(lucro);