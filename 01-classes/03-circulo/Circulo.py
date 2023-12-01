'''
    Crie uma classe Círculo com um método
    que calcule a área do círculo com base
    no raio fornecido.
'''
from math import pi

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return pi * self.raio ** 2
    
    def calcular_perimetro(self):
        return 2 * pi * self.raio