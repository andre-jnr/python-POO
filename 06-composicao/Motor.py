'''
    Crie uma classe Motor e uma classe
    Carro que possui um objeto do tipo
    Motor como atributo. A classe Carro
    deve ter métodos para ligar, desligar
    o motor, etc.
'''
class Motor:
    def __init__(self):
        self.ligado = False

    def ligar(self):
        if not self.ligado:
            print("Motor ligado.")
            self.ligado = True
        else:
            print("O motor já está ligado.")

    def desligar(self):
        if self.ligado:
            print("Motor desligado.")
            self.ligado = False
        else:
            print("O motor já está desligado.")