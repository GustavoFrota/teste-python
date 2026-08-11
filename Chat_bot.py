print("Chatbot iniciado! Digite 'sair' para encerrar.")

while True:
    mensagem = input("Você: ").strip().lower()

    match mensagem:

     case "oi" | "olá" | "ola":
        print("GSO: Olá, como posso ajudar?")

     case "como você está":
        print("GSO: estou funcionando perfeitamente")
    
     case "quem é você"| "quem é voce" | "quem é vc":
        print("GSO: me chamo GSO, um chatbot criado por Gustavo com respostas limitadas")
    
     case "sair":
        print("GSO: Programa encerrado, até logo.")
        break

     case _:
        print("GSO: desculpe, não entendi sua pergunta.")