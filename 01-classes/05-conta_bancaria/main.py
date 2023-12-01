'''
    Crie uma classe ContaBancaria com métodos
    para depósito, saque e verificação de saldo.
'''
from ContaBancaria import ContaBancaria

conta_bancaria = ContaBancaria(0)

conta_bancaria.depositar(100)
print(conta_bancaria)
conta_bancaria.sacar(75)
print(conta_bancaria)
