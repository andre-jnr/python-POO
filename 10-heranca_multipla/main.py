'''
    Explore herança múltipla criando uma classe
    Trabalhador que herda de classes como Pessoa
    e Funcionario, onde Pessoa é uma classe base
    e Funcionario é uma classe com informações
    específicas de emprego
'''
from Trabalhador import Trabalhador

trabalhador = Trabalhador("João", 30, 5000, "Analista")
print(trabalhador)
