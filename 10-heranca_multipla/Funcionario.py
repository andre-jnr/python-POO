'''
    Explore herança múltipla criando uma classe
    Trabalhador que herda de classes como Pessoa
    e Funcionario, onde Pessoa é uma classe base
    e Funcionario é uma classe com informações
    específicas de emprego
'''
class Funcionario:
    def __init__(self, salario, cargo):
        self.salario = salario
        self.cargo = cargo

    def __str__(self):
        return f"Funcionário: Salário R${self.salario}, Cargo: {self.cargo}"
