from time import sleep

def chatbot():
    print('Chatbot iniciado! Digite "sair" para encerrar o programa')

    while True:
        mensagem = input('Você: ').strip().lower()

        match mensagem:
            case 'sair':
                sleep(1)
                print('GSO: Programa encerrado!')
                break

chatbot()