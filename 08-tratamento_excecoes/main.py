from ContaBancaria import ContaBancaria

conta = ContaBancaria(100)
conta.checar_saldo()

conta.depositar(50)
conta.checar_saldo()

conta.sacar(30)
conta.checar_saldo()

conta.sacar(200)
conta.checar_saldo()