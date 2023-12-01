'''
    Crie uma classe Livro com atributos como
    título, autor e método para emprestar o livro.
'''
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.emprestado = False


    def emprestar(self):
        if not self.emprestado:
            self.emprestado = True
            print(f'O livro "{self.titulo}" foi emprestado.')
        else:
            print(f'O livro "{self.titulo}" já está emprestado.')

    def devolver(self):
        if self.emprestado:
            self.emprestado = False
            print(f'O livro "{self.titulo}" foi devolvido.')
        else:
            print(f'O livro "{self.titulo}" não estava emprestado.')