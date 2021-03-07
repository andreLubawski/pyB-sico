from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['nome'] = 'andré'
print(dicionario['sobrenome'])
print(dicionario)

# é uma forma de evitar o key error
