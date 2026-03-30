class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    def mostrar_saldo(self):
        return f"{self.titular}: R${self.__saldo}"

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print("Saldo insuficiente ou valor inválido.")
Conta = ContaBancaria("Ana", 1000)
print(Conta.mostrar_saldo())