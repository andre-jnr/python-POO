'''
    Crie uma classe Aluno que herde da classe Pessoa,
    adicionando atributos específicos como matrícula
    e métodos para exibir informações do aluno.
'''
from Pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def exibirInfo(self):
        print(f'Matricula: {self.matricula}')
        print(f'Nome: {self.nome}')
        print(f'Idade {self.idade}')