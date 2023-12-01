'''
    Na classe ContaBancaria do exercício 3,
    adicione tratamento de exceções para
    operações de saque que excedam o saldo disponível.
'''
class ContaBancaria:
    def __init__(self, saldo_inicial=0):
        self.__saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser maior que zero.")

    def sacar(self, valor):
        try:
            if valor > self.__saldo:
                raise ValueError("Saldo insuficiente para realizar o saque.")
            else:
                self.__saldo -= valor
                print(f"Saque de R${valor} realizado com sucesso.")
        except ValueError as e:
            print(e)

    def checar_saldo(self):
        print(f"Saldo disponível: R${self.__saldo}")
