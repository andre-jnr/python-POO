from produto import Produto


class Arquivo:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo

    def arquivoExiste(self):
        try:
            with open(self.nome_arquivo, 'r') as file:
                file.read()
        except FileNotFoundError:
            with open(self.nome_arquivo, 'w') as file:
                file.write('')
        else:
            return

    def adicionarProduto(self, produto):
        try:
            with open(self.nome_arquivo, 'a') as file:
                produto = Produto(produto.codigo, produto.descrição, produto.custo,
                                  produto.venda, produto.quantidade)
                file.write(str(produto))
        except:
            print('Houve um erro ao tentar ler o arquivo!')
        else:
            print(f'{produto.descrição} adicionado com sucesso!')
            print(f'Códido criado: {produto.codigo}')

    def listarProdutos(self):
        produtos = []
        with open(self.nome_arquivo, "r") as file:
            for linha in file:
                codigo, descricao, custo, venda, markup, quantidade = linha.strip().split(';')

                custo = float(custo)
                venda = float(venda)
                quantidade = int(quantidade)

                produto = Produto(codigo, descricao, custo, venda, quantidade)
                produtos.append(produto)
        return produtos

    def mostrarProdutos(self):
        try:
            a = open(self.nome_arquivo, 'r')
        except:
            print('Houve um erro ao tentar ler o arquivo!')
        else:
            print('-----PRODUTOS-----')
            for linha in a:
                dado = linha.split(';')
                print(f'Código: {dado[0]}')
                print(f'Descrição: {dado[1]}')
                print(f'Preço de custo: R${dado[2]}')
                print(f'Preço de venda R${dado[3]}')
                print(f'Margem de lucro R${dado[4]}%')
                print(f'Estoque: {dado[5]}')
                print('--------------------------------')

    def excluirProduto(self, codigo):
        produtos = self.listarProdutos()
        for produto in produtos:
            if int(produto.codigo) == codigo:
                print(f'{produto.descrição} excluido com sucesso')
                produtos.remove(produto)
                self.salvarProdutos(produtos)
                return True
        return False

    def salvarProdutos(self, produtos):
        with open(self.nome_arquivo, 'w') as file:
            for produto in produtos:
                file.write(str(produto))

    def realizarVenda(self, codigo, quantidade):
        produtos = self.listarProdutos()
        for produto in produtos:
            if int(produto.codigo) == codigo:
                produto.quantidade -= quantidade
                print(f'Descrição: {produto.descrição}')
                print(f'Estoque atual: {produto.quantidade}')
                self.salvarProdutos(produtos)
                return True
        return False

    def realizarCompra(self, codigo, quantidade):
        produtos = self.listarProdutos()
        for produto in produtos:
            if int(produto.codigo) == codigo:
                produto.quantidade += quantidade
                print(f'Descrição: {produto.descrição}')
                print(f'Estoque atual: {produto.quantidade}')
                self.salvarProdutos(produtos)
                return True
        return False
