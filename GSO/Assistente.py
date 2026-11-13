from time import sleep

def calcular():
    print('Iniciando calculadora')
    print(""" 
    SOMA(+)
    SUBTRAÇÃO(-)
    MULTIPLICAÇÃO(*)
    DIVISÃO(/)
    EXPONENCIAÇÃO(**)""")
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    operacao = input('Digite o sinal de operação: ')

    if operacao == '+':
        print(f'A soma de {n1} + {n2} é {n1+n2:.2f}')
    elif operacao == '-':
        print(f'A subtração de {n1} - {n2} é {n1-n2:.2f}')
    elif operacao == '*':
        print(f'A multiplicação de {n1} * {n2} é {n1*n2:.2f}')
    elif operacao == '/':
        if n2 ==0:
            print('ERRO: Impossível dividir por ZERO!')
        else:
            print(f'A divisão de {n1} / {n2} é {n1/n2:.2f}')
    elif operacao == '**':
        print(f'A exponenciação de {n1} ** {n2} é {n1**n2}')
    else:
        print('Sinal de Operação inválido')


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