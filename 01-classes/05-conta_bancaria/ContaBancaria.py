'''
    Crie uma classe ContaBancaria com métodos
    para depósito, saque e verificação de saldo.
'''
class ContaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo

    
    def depositar(self, valor):
        self.saldo += valor


    def sacar(self, valor):
        self.saldo -= valor


    # Como eu já estudei métodos especiais, achei útil treinar ele aqui
    def __str__(self):
        return f'Saldo: R${self.saldo}'
