'''
    Crie uma classe Animal com métodos comuns
    como fazer_som(). Em seguida, crie
    subclasses como Cachorro, Gato que sobrescrevem
    esse método para emitir sons específicos.
'''
from Cachorro import Cachorro
from Gato import Gato

cachorro = Cachorro('Sandy')
gato = Gato('Cleiton')

print(f'Cachorro começou a lati: {cachorro.fazerSom()}')
print(f'Gato começou a miar: {gato.fazerSom()}')
