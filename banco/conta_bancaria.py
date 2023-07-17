# Projeto de conta bancária
# Atributos: nome, saldo
# Métodos: mostrar saldo, sacar, depositar

# Adicionar novas funções:
# 1. historico de depositos e saques - ok
# 2. Taxas para saque - ok
# 3. Limite o saque após sacar o valor X - ok
# 4. Transferencia entre contas - OK

class ContaBancaria:
    historico = []

    def __init__(self, nome_titular, saldo_inicial):
        self.nome_titular = nome_titular
        self.saldo = saldo_inicial

    def exibirSaldo(self):
        print(f"Saldo atual: R$ {self.saldo:.2f}")

    def depositar(self, valor_deposito):
        self.saldo += valor_deposito
        print(f"Valor R$ {valor_deposito:.2f} foi depositado!")
        self.historico.append(valor_deposito)
        self.historico.append(self.saldo)
        self.exibirSaldo()

    def sacar(self, valor_saque):
        taxa = valor_saque * 0.10
        if (valor_saque + taxa) > self.saldo:
            print("Saldo insuficiente!")
        elif (valor_saque > 1000):
            print("Limite de saque atingido!")
        else:
            self.saldo -= (valor_saque + taxa)
            print(f"Valor R$ {valor_saque:.2f} foi sacado!")
            print(f"Com taxa de 10% no valor de R$ {taxa:.2f}")
            self.historico.append(valor_saque * -1)
            self.historico.append(self.saldo)
            self.exibirSaldo()

    def transferencia(self, valor_transf, conta):
        if valor_transf > self.saldo:
            print('Saldo insuficiente!')
        else:
            print(f'O valor de R$ {valor_transf:.2f}', end=' ')
            print(f'foi transferido para {conta}')
            self.saldo -= valor_transf
            conta.saldo += valor_transf
            self.exibirSaldo()

    def exibirHistorico(self):
        print('------EXTRATO------')
        for indice, operação in enumerate(self.historico):
            if indice % 2 == 0:
                if operação > 0:
                    print(f'Foi depositado R$ {operação:.2f}')
                else:
                    print(f'Foi sacado R$ {operação:.2f}', end=' ')
                    print(f'com uma taxa de R$ {abs(operação) * 0.10:.2f}')
            else:
                print(f'Saldo: R$ {operação:.2f}')
                print('-------------------')
