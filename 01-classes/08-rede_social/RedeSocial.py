'''
    Crie uma classe RedeSocial para representar
    uma rede social simples com métodos para
    adicionar amigos, postar mensagens etc.
'''
class RedeSocial:
    def __init__(self, user):
        self.user = user
        self.amigos = list()
        self.publicados = 0


    def adicionarAmigo(self, amigo):
        self.amigos.append(amigo)
        print(f'{amigo} adicionado me sua lista de amigos')


    def postarMensagem(self, string):
        print('Mensagem postada')
        self.publicados += 1
        print(string)


    def listarAmigos(self):
        string = ''

        for i in range(len(self.amigos)):
            if i != len(self.amigos) - 1:
                string += f'{self.amigos[i]}, '
            else:
                string += f'{self.amigos[i]}.'

        return string


    def estatisticas(self):
        print(f'User name: {self.user}')
        print(f'Quantidade de amigos: {len(self.amigos)}')
        print(f'Amigos: {self.listarAmigos()}')
        print(f'Quantidade de publicações: {self.publicados}')
