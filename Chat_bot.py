while True:
    mensagem = input("Você: ").strip().lower()

    match mensagem:

     case "oi" | "olá" | "ola":
        print("GSO: Olá, como posso ajudar?")

     case "como você está":
        print("GSO: estou funcionando perfeitamente")
    
     case "quem é você":
        print("GSO: me chamo GSO, um chatbot criado por Gustavo com respostas limitadas")
    
     case "sair":
        print("GSO: até logo.")
        break

     case _:
        print("GSO: desculpe, não entendi sua pergunta.")