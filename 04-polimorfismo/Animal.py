'''
    Crie uma classe Animal com métodos comuns
    como fazer_som(). Em seguida, crie
    subclasses como Cachorro, Gato que sobrescrevem
    esse método para emitir sons específicos.
'''
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazerSom(self):
        pass
