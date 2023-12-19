'''
  Crie uma classe Produto com atributos como nome,
  preço e método para aplicar desconto no preço.
'''


class Produto:
    def __init__(self, descricao, preco_un, qtde):
        self.descricao = descricao
        self.preco_un = preco_un
        self.qtde = qtde
        self.promocao = False
        self.log_preco = [self.preco_un, self.promocao]

    def aplicar_promocao(self, valor, tipo='percentual'):
        self.promocao = True
        if tipo == 'percentual':
            valor_desconto = self.preco_un * valor / 100
        elif tipo == 'preco':
            valor_desconto = valor
        else:
            raise ValueError('Tipo de promoção inválido')

        self.preco_un -= valor_desconto
        self.log_preco = [self.preco_un, self.promocao]

    def remover_promocao(self):
        for i in range(len(self.log_preco) - 2, 0, -2):
            if not self.log_preco[i]:
                self.preco_un, self.promocao = self.log_preco[i - 1], False
                self.log_preco = [self.preco_un, self.promocao]
                break

    def venda(self, qtde_venda):
        if qtde_venda < self.qtde:
            self.qtde -= qtde_venda
        else:
            raise ValueError('Estoque baixo')


if __name__ == '__main__':
    arroz = Produto('arroz', 100, 100)
    arroz.aplicar_promocao(10, tipo='preco')
    print(arroz.preco_un)
    arroz.aplicar_promocao(10, tipo='preco')
    print(arroz.preco_un)
    arroz.aplicar_promocao(10, tipo='preco')
    print(arroz.preco_un)
    arroz.remover_promocao()
    print(arroz.preco_un)
    print(arroz.log_preco)
    arroz.remover_promocao()
    print(arroz.preco_un)
    print(arroz.log_preco)

    print(arroz.qtde)
    arroz.venda(10)
    print(arroz.qtde)

    try:
        arroz.venda(200)
    except ValueError as e:
        print(f'Erro: {e}')
