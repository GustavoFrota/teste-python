def identificacao():
    nome = input("Digite o seu nome: ")
    sobrenome = input("Digite o seu sobrenome: ")

    NomeCompleto = nome + " " + sobrenome

    idade = int(input("Digite sua idade: "))

    print(f'Bem-vindo {NomeCompleto}!')

    if idade >=18:
        print(f'{nome} é maior de idade.')
    else:
        print(f'{nome} é menor de idade.')

identificacao()