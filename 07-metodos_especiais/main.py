'''
    Implemente métodos especiais como __str__,
    __eq__, __lt__, etc., em uma classe Produto,
    para representar produtos e realizar comparações
    entre eles
'''
from Produto import Produto

produto1 = Produto("Camiseta", 29.99, 1001)
produto2 = Produto("Calça Jeans", 49.99, 1002)
produto3 = Produto("Camiseta", 29.99, 1003)

# método __str__
print(produto1)
print(produto2)

# Testando igualdade entre produtos __eq__
print(produto1 == produto3)

# Testando comparação de preços __lt__
print(produto1 < produto2)