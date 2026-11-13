from time import sleep

def calcular():
    print('Iniciando calculadora')
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))

    print(f'A soma dos números {n1} e {n2} é {n1 + n2}')

def chatbot():
    print('Chatbot iniciado! Digite "sair" para encerrar o programa')

    while True:
        mensagem = input('Você: ').strip().lower()

        match mensagem:
            case 'sair':
                sleep(1)
                print('GSO: Programa encerrado!')
                break
            case 'calcular':
                calcular()

chatbot()