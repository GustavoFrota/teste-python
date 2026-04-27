n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
resultado = input("Digite a operação: ")

match resultado:
    case "+":
        resultado = n1 + n2
    case "-":
        resultado = n1 - n2
    case "*":
        resultado = n1 * n2
    case "/":
        if n2 != 0:
            resultado = n1 / n2
        else:
            resultado = "Erro: não é possível dividir com zero."
    case "_":
        resultado = "Operação inválida"

print(f'O resultado de {n1} e {n2} é: {resultado}')
    