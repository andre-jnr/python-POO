'''
    Crie uma classe Carro com métodos para
    ligar, desligar, acelerar e desacelerar.
'''
class Carro:
    def __init__(self):
        self.velocidade = 0
        self.ligado = False

    def ligar(self):
        if not self.ligado:
            print('Ligando carro...')
            self.ligado = True
        else:
            print('O carro já está ligado!')


    def desligar(self):
        if self.ligado:
            self.ligado = False
            self.velocidade = 0
        else:
            print('Carro já está desligado!')


    def acelerar(self):
        if self.ligado:
            self.velocidade += 10
        else:
            print('Ligue o carro para poder acelerar!')


    def desacelerar(self):
        if self.ligado:
            self.velocidade -= 10 if self.velocidade > 0 else 0
        else:
            print('Ligue o carro para poder acelerar!')


    def __str__(self):
        return f'Carro está a {self.velocidade}K/h'