for i in range(10):
    print("testando")

lista_precos = [1500, 1000, 800, 2000]

taxa_imposto = 0.1

for preco in lista_precos:
    imposto = preco * taxa_imposto
    print(f"Preço do produto {preco}, imposto do produto {imposto}")