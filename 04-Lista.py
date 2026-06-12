vendas = [100, 50, 1000, 800, 35]

print(vendas[0])

qtde_vendas = len(vendas);

total_vendas = sum(vendas) #sum é usada para somar os elementos
print(total_vendas)

media = total_vendas / qtde_vendas

print(media);

lista_produtos = ['iphone', 'ipad', 'apple watch', 'airpod', 'macbook']
print('macbook' in lista_produtos) #irá retornor True