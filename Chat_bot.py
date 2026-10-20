from time import sleep

def chatbot():
 print("Chatbot iniciado! Digite 'sair' para encerrar.")

 while True:
    mensagem = input("Você: ").strip().lower()

    match mensagem:

     case "oi" | "olá" | "ola":
        sleep(1)
        print("GSO: Olá, como posso ajudar?")

     case "como você está" | "como vc está" | "como vai" | "como vc esta" | "como voce esta":
        sleep(1)
        print("GSO: estou funcionando perfeitamente")

     case "Tudo bem" | "Tudo bom" | "Tá tudo bem":
          sleep(1)
          print("GSO: Tudo ótimo por aqui!")
          
     case "quem é você"| "quem é voce" | "quem é vc":
        sleep(1)
        print("GSO: me chamo GSO, um chatbot criado por Gustavo com respostas limitadas")

     case "sair" | "tchau":
        print("GSO: Programa encerrado, até logo.")
        break

     case _:
        sleep(1)
        print("GSO: desculpe, não entendi sua pergunta.")

chatbot()