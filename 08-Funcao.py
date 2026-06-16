lista_precos = [1500, 1000, 800, 2000]

def calcular_imposto(lista_valores):
    imposto_total = 0
    for preco in lista_valores:
        if preco > 1000:
            taxa = 0.15
        else:
            taxa = 0.1
        imposto = preco * taxa
        imposto_total += imposto


    return imposto_total

calcular_imposto(lista_precos)