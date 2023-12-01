'''
    Crie uma classe Triângulo com métodos
    para calcular área e perímetro com
    base nos comprimentos dos lados.
'''
from Triangulo import Triangulo

lado1 = 3
lado2 = 4
lado3 = 5

triangulo = Triangulo(lado1, lado2, lado3)
print("Perímetro:", triangulo.calcular_perimetro())
print("Área:", triangulo.calcular_area())
