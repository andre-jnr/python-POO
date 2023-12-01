'''
    Crie uma interface chamada FormaGeometrica
    com métodos como calcular_area() e
    calcular_perimetro(), e implemente essa
    interface em classes como Quadrado, Círculo, etc.
'''
from Circulo import Circulo
from Quadrado import Quadrado

quadrado = Quadrado(5)
print("Quadrado - Área:", quadrado.calcular_area())
print("Quadrado - Perímetro:", quadrado.calcular_perimetro())

circulo = Circulo(3)
print("\nCírculo - Área:", circulo.calcular_area())
print("Círculo - Perímetro:", circulo.calcular_perimetro())
