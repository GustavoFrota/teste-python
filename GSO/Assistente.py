from time import sleep

gso = 'GSO>' # Variável global

def calculadora():
  try:
    print('Iniciando calculadora')
    print(""" 
    SOMA(+)
    SUBTRAÇÃO(-)
    MULTIPLICAÇÃO(*)
    DIVISÃO(/)
    EXPONENCIAÇÃO(**)""")
    n1 = float(input(f'{gso} Digite o primeiro número: '))
    n2 = float(input(f'{gso} Digite o segundo número: '))
    operacao = input(f'{gso} Digite o sinal de operação: ')

    if operacao == '+':
        print(f'{gso} A soma de {n1} + {n2} é {n1+n2:.2f}')
    elif operacao == '-':
        print(f'{gso} A subtração de {n1} - {n2} é {n1-n2:.2f}')
    elif operacao == '*':
        print(f'{gso} A multiplicação de {n1} * {n2} é {n1*n2:.2f}')
    elif operacao == '/':
        if n2 ==0:
            print('ERRO: Impossível dividir por ZERO!')
        else:
            print(f'{gso} A divisão de {n1} / {n2} é {n1/n2:.2f}')
    elif operacao == '**':
        print(f'{gso} A exponenciação de {n1} ** {n2} é {n1**n2}')
    else:
        print('ERRO: Sinal de Operação inválido')
  except ValueError:
      print('ERRO: Você precisa digitar números válidos')

def imc():
   try:
    nome = input(f'{gso} Digite o seu nome: ')
    peso = float(input(f'{gso} Digite o seu peso: '))
    altura = float(input(f'{gso} Digite a sua altura: '))
    IMC = peso / (altura**2)

    print(f'{gso} O imc de {nome} é {IMC:.2f}')

    if IMC < 18.5:
        print(f'{gso} Situação: Abaixo do peso.')
    elif IMC < 25:
        print(f'{gso} Situação: Peso normal.')
    elif IMC < 30:
        print(f'{gso} Situação: Sobrepeso.')
    else:
        print(f'{gso} Situação: Obesidade.')
   except ValueError:
       print('ERRO: Digite valores númericos válidos!')

def chatbot():
    print('Chatbot iniciado! Digite "sair" para encerrar o programa')
    print("""Programas:
Calcular
imc
""")

    while True:
        mensagem = input('Você> ').strip().lower()

        match mensagem:
            case 'sair' | 'cls':
                sleep(1)
                print(f'{gso} Programa encerrado!')
                break

            case 'calcular':
                sleep(1)
                calculadora()

            case 'imc':
                sleep(1)
                imc()

chatbot()