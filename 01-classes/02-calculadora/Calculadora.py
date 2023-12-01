'''
    Calculadora simples: Crie uma classe
    Calculadora com métodos para adição,
    subtração, multiplicação e divisão.
'''
class Calculadora:
    def __init__(self, a, b):
        self.a = a
        self.b = b


    def adicao(self):
        return self.a + self.b
    

    def subtracao(self):
        return self.a - self.b
    

    def multiplicacao(self):
        return self.a * self.b
    

    def divisao(self):
        return self.a / self.b