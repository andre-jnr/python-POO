'''
Crie programa que defina a classe "Círculo"
com un construtor que recebe
o raio do círculo.
O programa deve criar duas instâncias da classe
"Círculo", "c1" e "c2", com diferentes valores
para o parâmetro raio.
Em seguida, o programa deve imprimir o raio e
a área de cada um dos círculos criados.

A = pi * raio²
'''
from math import pi

class Circulo:
    def __init__(self, raio):
      self.raio = raio
      self.area = pi * raio * raio

c1 = Circulo(2)
c2 = Circulo(10)

print(c1.raio)
print(f"{c1.area}")
print("----------")
print(c2.raio)
print(f"{c2.area:.2f}")
