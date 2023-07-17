class Produto:
    def __init__(self, codigo, descrição, custo, venda, quantidade):
        self.codigo = codigo
        self.descrição = descrição
        self.custo = custo
        self.venda = venda
        self.markup = ((venda - custo) / custo) * 100
        self.quantidade = quantidade

    def __str__(self):
        return f'{self.codigo};{self.descrição};{self.custo:.2f};{self.venda:.2f};{self.markup:.2f};{self.quantidade}\n'
