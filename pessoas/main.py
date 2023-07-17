from pessoa import Pessoa

p1 = Pessoa('Junior', 20)
p2 = Pessoa.por_ano_nascimento('André', 2003)

print(
    f'Nome: {p1.nome} \n'
    f'idade: {p1.idade} \n'
)

print(
    f'Nome: {p2.nome} \n'
    f'idade: {p2.idade} \n'
)

print(Pessoa.gera_id())
