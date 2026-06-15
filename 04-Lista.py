vendas = [100, 50, 1000, 800, 35]

print(vendas[0])

qtde_vendas = len(vendas);

total_vendas = sum(vendas) #sum é usada para somar os elementos
print(total_vendas)

media = total_vendas / qtde_vendas

print(media);

lista_produtos = ['iphone', 'ipad', 'apple watch', 'airpod', 'macbook']
print('macbook' in lista_produtos) #irá retornor True

posicao = lista_produtos.index('macbook') #index serve para encontrar a posição de um alemento 
print(posicao) #irá retornar 4

lista_precos = [5000, 7000, 3000, 1000, 10000] #editando uma lista
novo_preco = lista_precos[0] * 1.1
lista_precos[0] = novo_preco
print(novo_preco);

#lista_produtos.remove('macbook') Removendo um item na lista
item_removido = lista_produtos.pop(4)
print(lista_produtos)
print(item_removido)

lista_produtos.append('iphone 17') #adicionando um item na lista
print(lista_produtos)

lista2_produtos = ['PC', 'air tag', 'monitor'] 
lista_produtos.extend(lista2_produtos) #juntando listas
print(lista_produtos)