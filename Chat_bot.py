while True:
    mensagem = input("Você: ").strip().lower()

    if mensagem == "oi" or mensagem == "olá" or mensagem == "ola":
        print("GSO: Olá, como posso ajudar?")

    elif mensagem == "como você está":
        print("GSO: estou funcionando perfeitamente")
    
    elif mensagem == "quem é você":
        print("GSO: me chamo GSO, um chatbot criado por Gustavo com respostas limitadas")
    
    elif mensagem == "sair":
        print("GSO: até logo.")
        break

    else:
        print("GSO: desculpe, não entendi sua pergunta.")