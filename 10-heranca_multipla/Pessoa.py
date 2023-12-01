'''
    Explore herança múltipla criando uma classe
    Trabalhador que herda de classes como Pessoa
    e Funcionario, onde Pessoa é uma classe base
    e Funcionario é uma classe com informações
    específicas de emprego
'''
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"Pessoa: {self.nome}, {self.idade} anos"
