# os sets seguem as regras dos conjuntos matemáticos
'''
con = set({1,1,1,2,14,23,0,4})
print(con)
con2 = {1,1,2}
print(con2)

lista = [1, 1, 1, 2, 3]
con3 = set(lista)
print(con3)

# obs: assim como nas outras coleções, posso usar vários tipos de dados num mesmo set

con3.remove(1)
# 1 é o valor, não o índice, afinal, conjuntos não são indexados
print(con3)
con3.discard((3))
print(con3)
con3.add(5)
print(con3)
'''
a = {'a', 2, 'd'}
b = {'w', 2312, 2, 'd'}
c = a.union(b)
print(c)
d = a.intersection(b)
print(d)


print(a|b)
# union

print(a.difference(b))
