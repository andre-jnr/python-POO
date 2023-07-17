class ContaBancaria:
    def __init__(self, nome_titular, saldo_inicial):
        self.nome_titular = nome_titular
        self.saldo = saldo_inicial
        self.saque_total = 0
        self.extrato = []

    def exibir_saldo(self):
        print(f"Saldo atual: R$ {self.saldo}")

    def depositar(self, valor_deposito):
        self.saldo += valor_deposito
        self.extrato.append("+ R$ " + str(valor_deposito))
        print(f"Valor R$ {valor_deposito} foi depositado!")
        self.exibir_saldo()

    def sacar(self, valor_saque):
        taxa = 5
        valor_taxa = valor_saque * (taxa/100)
        if (valor_saque+valor_taxa) > self.saldo:
            print("Saldo insuficiente!")
        else:
            self.saque_total += valor_saque
            limite = 100

            if (self.saque_total > limite):
                print("Limite atingido!!")
            else:
                self.extrato.append("- R$ " + str(valor_saque+valor_taxa))
                self.saldo -= (valor_saque + valor_taxa)
                print(f"Valor R$ {valor_saque} foi retirado da conta!")
                print(f"Taxa: R$ {valor_taxa}")
                self.exibir_saldo()

    def exibir_extrato(self):
        print("\nEXTRATO:")
        for item in self.extrato:
            print(item)

    def transferir(self, valor_transf, conta_destino):
        self.saldo -= valor_transf
        conta_destino.depositar(valor_transf)
        print(f"Transferencia de {valor_transf} realizada!")
        self.extrato.append("- R$ " + str(valor_transf))
