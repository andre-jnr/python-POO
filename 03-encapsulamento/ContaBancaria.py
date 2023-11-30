'''
    Crie uma classe ContaBancaria com métodos para depositar,
    sacar e checar saldo, mantendo o saldo como um atributo privado.
'''
class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if valor > self.__saldo:
            print("Saldo insuficiente.")
        else:
            self.__saldo -= valor

    def checarSaldo(self):
        print(f'Saldo atual: R${self.__saldo}')
