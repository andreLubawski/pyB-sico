# dicionários são semelhantes aos mapas de outras linguagens
# são coleções do tipo {chave: valor}

"""print(type({}))

paises = {'br': 'Brasil', 'eua': 'Estados Unidos'}
print(paises)
# tanto chave quanto valor podem ser de qualquer tipo
"""
# paises2 = dict(br='Brasil', eua='Estados Unidos', fr='França')
"""print(paises2)

print(paises2['fr'])
print(paises2.get('br'))
"""
"""
tipo None: um 'tipo sem tipo'
numeros = None
print(numeros)
print(type(numeros))
"""
"""pais = paises2.get('fr', 'entrada incorreta')
print(f'encontrei o país: {pais}')
"""
'''
print('br' in paises2)


receita = {'jan': 100, 'fev': 120}
receita['mar'] = 500
novoMes = {'abr' : 200}
receita.update(novoMes)
print(receita)
receita['jan'] = 1000
print(receita)
receita.update({'fev': 900})
print(receita)
'''
'''
# remoção de elementos, passar a chave
corFrutas = dict(banana= 'amarela', uva= 'roxa')
corFrutas.pop('banana')
print(corFrutas)
del corFrutas['uva']
print(corFrutas)
corFrutas['morango'] = 'vermelho'
print(corFrutas)



user = {}.fromkeys('nome', 'pontos')
print(user)
# cada elemento de nome vira uma chave
user2 = {}.fromkeys(['nome'], 'andré')
#para o caso ['nomeee'] não seriam geradas chaves repetidas
print(user2)
ex = {}.fromkeys(range(1,11), 'novo')
print(ex)

'''
receita = {'jan': 100, 'fev': 200}
'''for key in receita:
    print(key)
for key in receita:
    print(receita[key])

print(receita.keys())'''
for key in receita.keys():
    print(key)
for values in receita.values():
    print(values)

for key, values in receita.items():
    print(f'key={key} value={values}')

print(sum(receita.values()))

print(len(receita))