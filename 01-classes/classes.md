# Classes

Em POO, uma classe é um modelo que define as características e comportamentos de um objeto. Em Python, uma classe é declarada usando a palavra-chave `class`.

Por exemplo, a seguinte classe define um objeto `Carro`:

```python
class Carro:
    def __init__(self, cor, modelo):
        self.cor = cor
        self.modelo = modelo
        self.farois_ligados = False

    def acelerar(self):
        print(f"O {self.modelo} está acelerando!")
```

Essa classe define dois atributos: `cor` e `modelo`. Esses atributos representam o estado do objeto `Carro`. A classe também define um método: `acelerar()`. Esse método representa o comportamento do objeto `Carro`.

Por exemplo, o seguinte código cria um objeto `Carro` vermelho com o modelo "Gol":

```python
carro = Carro("vermelho", "Gol")
```

A variável `carro` agora aponta para um objeto `Carro`. Podemos acessar os atributos e métodos do objeto usando a notação de ponto. Por exemplo, o seguinte código imprime a cor do carro:

```python
print(carro.cor)
# Output: vermelho
```

Podemos chamar o método `acelerar()` do objeto usando a notação de ponto. Por exemplo, o seguinte código imprime uma mensagem informando que o carro está acelerando:

```python
carro.acelerar()
# Output: O Gol está acelerando!
```

As classes são uma ferramenta poderosa que nos permitem criar programas mais organizados e reutilizáveis. Elas nos permitem agrupar atributos e métodos relacionados em um único lugar, o que facilita a manutenção e a compreensão do código. Além disso, as classes nos permitem criar objetos que podem ser reutilizados em diferentes partes do programa.

Aqui estão alguns exemplos de como as classes podem ser usadas em Python:

- Podemos usar classes para representar entidades do mundo real, como carros, pessoas ou empresas.
- Podemos usar classes para criar estruturas de dados complexas, como listas, árvores e gráficos.
- Podemos usar classes para criar sistemas de software modulares e reutilizáveis.

A POO é um paradigma de programação poderoso que pode ser usado para criar programas mais eficientes e eficazes.

# Exercicios

1. [Criar uma classe Pessoa](01-pessoa/Pessoa.py): Crie uma classe Pessoa com atributos como nome, idade e método para imprimir informações básicas sobre a pessoa.

1. [Calculadora simples](02-calculadora/Calculadora.py): Crie uma classe Calculadora com métodos para adição, subtração, multiplicação e divisão.

1. [Círculo](03-circulo/Circulo.py): Crie uma classe Círculo com um método que calcule a área do círculo com base no raio fornecido.

1. [Livro](04-livro/Livro.py): Crie uma classe Livro com atributos como título, autor e método para emprestar o livro.

1. [Conta bancária](05-conta_bancaria/ContaBancaria.py): Crie uma classe ContaBancaria com métodos para depósito, saque e verificação de saldo.

1. [Triângulo](06-triangulo/Triangulo.py): Crie uma classe Triângulo com métodos para calcular área e perímetro com base nos comprimentos dos lados.

1. [Carro](07-carro/Carro.py): Crie uma classe Carro com métodos para ligar, desligar, acelerar e desacelerar.

1. [Rede social](08-rede_social/RedeSocial.py): Crie uma classe RedeSocial para representar uma rede social simples com métodos para adicionar amigos, postar mensagens etc.

1. [Jogo de cartas](09-jogo_cartas/Carta.py): Crie uma classe Carta para representar uma carta de baralho com atributos como valor e naipe.

1. [Produto](10-produto/Produto.py): Crie uma classe Produto com atributos como nome, preço e método para aplicar desconto no preço.
