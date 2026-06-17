while True:
    mensagem = input("Você: ").lower()

    if mensagem == "oi":
        print("Bot: Olá, como posso ajudar?")
    elif mensagem == "como você está":
        print("bot: estou funcionando perfeitamente")
        break
    else:
        print("bot: desculpe, não entendi sua pergunta.")