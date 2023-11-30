from ContaBancaria import ContaBancaria

conta_bancaria = ContaBancaria(0)

while True:
    print('O que deseja realizar?')
    print('[1] - Consultar')
    print('[2] - Depositar')
    print('[3] - Sacar')
    print('[4] - Sair')
    opcao = input('-> ')

    match opcao:
        case '1':
            conta_bancaria.checarSaldo()
        case '2':
            valor = float(input('Digite o valor do deposito: R$'))
            conta_bancaria.depositar(valor)
        case '3':
            valor = float(input('Digite o valor do saque: R$'))
            conta_bancaria.sacar(valor)
        case '4':
            print('Programa encerrado...')
            print('Agradecemos a preferência :)')
            break
        case _:
            print('Opção inválida!')