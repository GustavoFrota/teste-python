def identificacao():
    nome = input("Digite o seu nome: ")
    idade = int(input("Digite sua idade: "))

    print(f'Olá, me chamo {nome} e eu tenho {idade} anos')

    if idade >=18:
        print(f'{nome} é maior de idade.')
    else:
        print(f'{nome} é menor de idade.')

identificacao()