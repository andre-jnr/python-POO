'''
    Implemente métodos especiais como __str__,
    __eq__, __lt__, etc., em uma classe Produto,
    para representar produtos e realizar comparações
    entre eles
'''
class Produto:
    def __init__(self, nome, preco, codigo):
        self.nome = nome
        self.preco = preco
        self.codigo = codigo

    def __str__(self):
        return f"Produto: {self.nome} - Preço: R${self.preco:.2f} - Código: {self.codigo}"

    def __eq__(self, codigo_outro_produto):
        return self.codigo == codigo_outro_produto.codigo

    def __lt__(self, preco_outro_produto):
        return self.preco < preco_outro_produto.preco
       