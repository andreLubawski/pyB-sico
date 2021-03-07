from collections import OrderedDict
# garante que a exibição será feita conforme minha inserção
d1 = OrderedDict({'a': 1, 'b': 2, 'd': 4, 'c': 3})

for key, value in d1.items():
    print(f'chave:{key} valor:{value}')

