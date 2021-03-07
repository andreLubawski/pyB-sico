from collections import namedtuple

cachorro = namedtuple('cachorro', 'idade raca nome')
cachorro2 = namedtuple('cachorro', 'idade, raca, nome')
cachorro3 = namedtuple('cachorro', ['idade', 'nome', 'raca'])

a = cachorro(idade=2, raca='qualquerUma', nome='abc')
print(a)
print(a[0])
print(a.idade)
