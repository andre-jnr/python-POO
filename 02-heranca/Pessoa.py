'''
    Criação de uma Classe Básica:
    Crie uma classe chamada Pessoa com métodos para
    definir nome, idade e método para exibir informações.
'''
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = str(nome)
        self.idade = int(idade)

    def exibirInfo(self):
        print(f'Nome: {self.nome}')
        print(f'Idade {self.idade}')
