from produto import Produto
from arquivo import Arquivo
arquivo = Arquivo('base-dados.txt')


class Menu:
    def menu(self):
        from os import system
        system('cls')
        print('1 - Cadastrar produto')
        print('2 - Entrada no estoque')
        print('3 - Realizar venda')
        print('4 - Exibir produtos')
        print('5 - Excluir produto')
        print('6 - Sair do sistema')

        while True:
            opção = str(input('-> '))
            if opção in ['1', '2', '3', '4', '5', '6']:
                break

        return opção

    def verificarId(self, codigo):
        produtos = arquivo.listarProdutos()
        for produto in produtos:
            if int(produto.codigo) == int(codigo):
                return False
        return True

    def gerarId(self, nome_arquivo):
        controle = 0
        while True:
            controle += 1
            with open(nome_arquivo, 'r') as arquivo:
                linhas = arquivo.readlines()
                codigo = len(linhas) + controle
                if self.verificarId(codigo):
                    return int(codigo)

    def opções(self, opção, nome_arquivo):
        from os import system
        system('cls')
        if opção == '1':
            codigo = self.gerarId('base-dados.txt')
            descrição = str(input('Digite o nome do produto: '))
            try:
                custo = str(input('Digite o preço de custo: '))
                custo = custo.replace(',', '.')
                print(custo)
                custo = float(custo)
                venda = str(input('Digite o preço de venda: '))
                print(venda)
                venda = venda.replace(',', '.')
                venda = float(venda)
            except:
                print('Algo deu errado :(')
                return False
            margem = ((venda - custo) / custo) * 100
            print(f'Sua margem de lucro ficará em {margem:.2f}%')
            estoque = 0
            produto = Produto(codigo, descrição, custo, venda, estoque)
            nome_arquivo.adicionarProduto(produto)
            return True
        elif opção == '2':
            try:
                codigo = int(
                    input('Digite o código do produto que você tará entrada: '))
                quantidade = int(input('Quantidade que entrará no estoque: '))
            except ValueError:
                print('Por favor, digite um número inteiro :(')
                return False
            if nome_arquivo.realizarCompra(codigo, quantidade):
                print('Entrada de produtos realizada com sucesso')
                return True
            else:
                print(f'Código {codigo} não encontrado :(')
                return False
        elif opção == '3':
            try:
                codigo = int(
                    input('Digite o códgio do produto que será vendido: '))
                quantidade = int(input('Quantidade que será vendida: '))
            except ValueError:
                print('Por favor, digite um número inteiro :(')
                return False
            if nome_arquivo.realizarVenda(codigo, quantidade):
                print('venda realizada com sucesso')
                return True
            else:
                print(f'Código {codigo} não encontrado :(')
                return False
        elif opção == '4':
            nome_arquivo.mostrarProdutos()
            return True
        elif opção == '5':
            try:
                codigo = int(
                    input('Digite o código do produto que você deseja EXCLUIR: '))
            except ValueError:
                print('Por favor, digite um número inteiro :(')
                return False
            if nome_arquivo.excluirProduto(codigo):
                print()
                return True
            else:
                print('produto não encontrado :(')
                return False
        elif opção == '6':
            return False

    def retornarAoMenu(self):
        print('---')
        print('Digite qualquer coisa pra sair, ou...')
        opção = str(input('Digite 1 para voltar ao menu principal: '))
        if opção == '1':
            return True
        else:
            return False
