from Pessoa import Pessoa

nome = str(input('Nome: '))
idade = int(input('Idade: '))
pessoa = Pessoa(nome, idade)
pessoa.exibirInfo()
