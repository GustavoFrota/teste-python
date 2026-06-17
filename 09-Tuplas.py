tupla_vendas = (1000, 800, 500)
print(tupla_vendas[0])

def calcular_bonus(lista_vendas):
    bonus1 = 2 * len(lista_vendas)
    bonus2 = 0.1 * sum(lista_vendas)
    return bonus1, bonus2

vendas = [100, 200, 400, 1000]
resultado = calcular_bonus(vendas)
print(resultado)