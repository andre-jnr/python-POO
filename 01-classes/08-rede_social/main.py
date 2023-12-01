'''
    Crie uma classe RedeSocial para representar
    uma rede social simples com métodos para
    adicionar amigos, postar mensagens etc.
'''
from RedeSocial import RedeSocial

usuario = RedeSocial('hey.junin')

usuario.adicionarAmigo('Juan')
usuario.adicionarAmigo('Rubens')
usuario.adicionarAmigo('Chris')
usuario.adicionarAmigo('Levy')

usuario.postarMensagem('Não acredito que estou namorando com uma mulher dessas!')
usuario.postarMensagem('Complicado ser romantico num seculo desses!')

usuario.estatisticas()
