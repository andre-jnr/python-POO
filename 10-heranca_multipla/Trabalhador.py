'''
    Explore herança múltipla criando uma classe
    Trabalhador que herda de classes como Pessoa
    e Funcionario, onde Pessoa é uma classe base
    e Funcionario é uma classe com informações
    específicas de emprego
'''
from Pessoa import Pessoa
from Funcionario import Funcionario

class Trabalhador(Pessoa, Funcionario):
    def __init__(self, nome, idade, salario, cargo):
        Pessoa.__init__(self, nome, idade)
        Funcionario.__init__(self, salario, cargo)

    def __str__(self):
        return f"{Pessoa.__str__(self)}, {Funcionario.__str__(self)}"
