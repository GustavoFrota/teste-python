print("Iniciando a calculadora")

try:
 n1 = float(input("Digite o primeiro número: "))
 operacao = input("Digite a operação: ")
 n2 = float(input("Digite o segundo número: "))


 match operacao:
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
            print("Erro: não é possível dividir com zero.")
    case "**":
        resultado = n1 ** n2
        print(f'A exponenciação de {n1} ** {n2} é {resultado}')
    case _:
        print("Operação inválida.")

except ValueError:
 print("Erro: você precisa digitar números válidos.")

 print("Encerrando a calculadora")