"""listas são semelhantes a vetores em outras
linguagens, com a diferença de serem dinâmicos e
aceitarem qualquer tipo de dado """

"""
l1 = [1, 23, 56, 2]
l2 = ['a', 300, 'wxya']
l3 = []

l4 = list(range(11))
print(l4)
l5 = list('andré')
print(l5)

print('a' in l5)
print(not(55 in l1))

l1.sort()
print(l1)
l1.reverse()
print(l1)
print(l1.count(23))

l2.append(32)
# com append, só consigo add um elemento por vez
print(l2)
l2.append(['a', 'b'])
print(l2)

l2.extend([1, 2, 3])
print(l2)
# os valores do elemento lista são add como elementos únicos
# extend só aceita valores iteráveis, como listas, strings, ...

l2.insert(0, 'abc')
print(l2)
# o valor em 0 é deslocado para a direita

print(l1+l2)


l6 = l2.copy()
print(l6)
print(len(l6))

l6.pop()
# remove o último elemento
print(l6)

l6.pop(0)
print(l6)

l6.clear()
print(l6)

l6 = [1, 2, 'a']
print(l6*4)

nome = 'andré,lubawski'
nomeList = nome.split(',')
print(nomeList)

l7 = ['programação', 'python']
novaStr = ' '.join(l7)
print(novaStr)

# iterações em listas

for elemento in l6:
    print(elemento)

carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto ou digite 'sair': ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)
for produto in carrinho:
    print(produto)
"""
cores = ['amarelo', 'verde', 'vermelho']
print(cores[-3])

for indice, cor in enumerate(cores):
    print(indice, cor)

print(cores.index("verde"))
print(cores.index('vermelho', 1))
# busca vermelho a partir do índice 1
print(cores.index('verde', 0, 2))
# busca verde entre os índices 0 e 2

print(cores[:: -1])


lista = [1, 2, 3]
print(sum(lista))
print(max(lista))
print(min(lista))
print(len(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

"""desempacotamento"""
n1, n2, n3 = lista
print(n1, n2, n3)


# cópia de listas

#deep copy
l = [1, 2, 3]
nova = l.copy()
nova.append(4)

print(l)
print(nova)

# shallow copy

l2 = [1, 2 , 3 , 4]
nova2 = l2
nova2.append(5)

print(l2)
print(nova2)