disc_produtos = {
    "ipad": 7000,
    "iphone": 5000,
    "airpod": 2000
}

print(disc_produtos["airpod"])

disc_vendas = {
    "Guilherme": [1000, 500, 1500],
    "João": [500, 450, 500]
}

print(disc_vendas["Guilherme"])

disc_produtos["iphone"] = disc_produtos["iphone"] * 1.1 #Modificando itens de um dicionário
print(disc_produtos["iphone"])

disc_produtos["macbook"] = 1200 #Adicionando um item ao dicionário
print(disc_produtos)

disc_produtos.pop("macbook") #Removendo um item do dicionário
print(disc_produtos)

print("iphone" in disc_produtos) #Verificando se um item existe no dicionário