from arquivo import Arquivo
from menu import Menu

arquivo = Arquivo('base-dados.txt')

menu = Menu()

while True:
    opção = menu.menu()
    menu.opções(opção, arquivo)
    if menu.retornarAoMenu():
        print()
    else:
        break
