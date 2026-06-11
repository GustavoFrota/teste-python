faturamento = 1000;
custo = 600;
lucro = faturamento - custo;
texto = f"O lucro foi de {lucro} e o faturamento foi de {faturamento}";
print(texto);

email = " EMAIL_FALSO@gmail.com ";

email = email.lower(); #lower converter todas as letras de uma string para minúsculas
email = email.strip(); #strip é usado para remover espaços em branco
print(email);

print(len(email)) #len é usada para contar a quantidade de elementos

posicao = email.find('@'); #find é usado para procurar uma substring dentro de uma string e retornar a posição onde ela começa.
print(posicao);