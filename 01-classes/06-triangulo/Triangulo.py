'''
    Crie uma classe Triângulo com métodos
    para calcular área e perímetro com
    base nos comprimentos dos lados.
'''
class Triangulo:
    def __init__(self, lado_a, lado_b, lado_c):
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.lado_c = lado_c

    def calcular_perimetro(self):
        return self.lado_a + self.lado_b + self.lado_c

    def calcular_area(self):
        s = self.calcular_perimetro() / 2
        area = (s * (s - self.lado_a) * (s - self.lado_b) * (s - self.lado_c)) ** 0.5
        return area
