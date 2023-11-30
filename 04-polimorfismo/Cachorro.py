'''
    Crie uma classe Animal com métodos comuns
    como fazer_som(). Em seguida, crie
    subclasses como Cachorro, Gato que sobrescrevem
    esse método para emitir sons específicos.
'''
from Animal import Animal

class Cachorro(Animal):
    def fazerSom(self):
        return 'Au au'
