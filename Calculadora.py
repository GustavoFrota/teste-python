n1 = int(input("Digite o primeiro número: "))
resultado = input("Digite a operação: ")
n2 = int(input("Digite o segundo número: "))


match resultado:
    case "+":
        resultado = n1 + n2
        print(f'A soma de {n1} + {n2} é {resultado}')
    case "-":
        resultado = n1 - n2
        print(f'A subtração de {n1} - {n2} é {resultado}')
    case "*":
        resultado = n1 * n2
        print(f'A multiplicação de {n1} * {n2} é {resultado}')
    case "/":
        if n2 != 0:
            resultado = n1 / n2
            print(f'A divisão de {n1} / {n2} é {resultado}')
        else:
            resultado = "Erro: não é possível dividir com zero."
    case "_":
        resultado = "Operação inválida."


    