print("Iniciando a calculadora")
n1 = float(input("Digite o primeiro número: "))
operacao = input("Digite a operação: ")
n2 = float(input("Digite o segundo número: "))


match operacao:
    case "+":
        resultado = n1 + n2
        print(f'A soma de {n1} + {n2} é {resultado}')
        print("Encerrando a calculadora")
    case "-":
        resultado = n1 - n2
        print(f'A subtração de {n1} - {n2} é {resultado}')
        print("Encerrando a calculadora")
    case "*":
        resultado = n1 * n2
        print(f'A multiplicação de {n1} * {n2} é {resultado}')
        print("Encerrando a calculadora")
    case "/":
        if n2 != 0:
            resultado = n1 / n2
            print(f'A divisão de {n1} / {n2} é {resultado}')
            print("Encerrando a calculadora")
        else:
            print("Erro: não é possível dividir com zero.")
    case "**":
        resultado = n1 ** n2
        print(f'A expexponenciação de {n1} ** {n2} é {resultado}')
        print("Encerrando a calculadora")
    case _:
        print("Operação inválida.")
