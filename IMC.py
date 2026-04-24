def calcular():
    nome = input("Digite o seu nome: ")
    peso = float(input("Digite o seu peso em kg: "))
    altura = float(input("Digite a sua altura em Metros: "))

    IMC = peso / (altura ** 2)

    print(f'O IMC de {nome} é {IMC:.2f}')

    if(IMC < 18.5):
        print('Situação: Abaixo do peso')
    elif(IMC < 25):
        print('Situação: Sobrepeso')
    elif(IMC <= 30):
        print('Situação: Peso normal')
    else:
        print('Situação: Abaixo do peso')
        
calcular()