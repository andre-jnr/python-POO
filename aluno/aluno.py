'''
Crie um prograna que defina a classe "Aluno" o
com um construtor que recebe três
O nome, a idade e a nota do aluno.
O progrua deve criar duas instâncias da classe
"Aluno", "a1" e "a2", com diferentes valores para
os parêmetros idade e nota.
Em seguida, o programa deve imprimir o nome,
a idade e a nota de cada un dos alunos criados.
E por último, calcular e imprimir a média das
notas dos dois alunos criados.
'''

class Aluno:
    def __init__(self, nome, idade, nota):
        self.nome = nome
        self.idade = idade
        self.nota = nota

a1 = Aluno("Layna", 8, 8.5)
a2 = Aluno("David", 9, 9.5)
media = (a1.nota + a2.nota) / 2

print(f"{a1.nome}\n{a1.idade}\n{a1.nota}\n \n{a2.nome}\n{a2.idade}\n{a2.nota}\n\n{media}")