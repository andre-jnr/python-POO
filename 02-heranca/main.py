from Aluno import Aluno

matricula = int(input('Digite a matricula: '))
nome = str(input('Digite o nome: '))
idade = int(input('Digite a idade: '))

print()

aluno = Aluno(nome, idade, matricula)
aluno.exibirInfo()