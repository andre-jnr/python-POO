'''
    Crie uma classe Círculo com um método
    que calcule a área do círculo com base
    no raio fornecido.
'''
from Circulo import Circulo

raio = float(input('Digite o valor do raio: '))
circulo = Circulo(raio)
print(f'Área do círculo: {circulo.calcular_area():.2f}')
