'''
    Crie uma classe Motor e uma classe
    Carro que possui um objeto do tipo
    Motor como atributo. A classe Carro
    deve ter métodos para ligar, desligar
    o motor, etc.
'''
from Motor import Motor

class Carro:
    def __init__(self):
        self.motor = Motor()

    def ligar_motor(self):
        self.motor.ligar()

    def desligar_motor(self):
        self.motor.desligar()