def calcular():
    nome = input("Digite o seu nome: ")
    peso = float(input("Digite o seu peso em kg: "))
    altura = float(input("Digite a sua altura em Metros: "))

    IMC = peso / (altura * altura)

    if(IMC >= 30):
        print(f'O IMC de {nome} é {IMC}')
        print('Situação: Obesidade')
    elif(IMC <= 29.9):
        print(f'O IMC de {nome} é {IMC}')
        print('Situação: Sobrepeso')
    elif(IMC <= 24.9):
        print(f'O IMC de {nome} é {IMC}')
        print('Situação: Peso normal')
    else:
        print(f'O IMC de {nome} é {IMC}')
        print('Situação: Abaixo do peso')
        
calcular()