from FormaGeometrica import FormaGeometrica
from math import pi
    
class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio
    
    def calcular_area(self):
        return pi * self.raio ** 2
    
    def calcular_perimetro(self):
        return 2 * pi * self.raio