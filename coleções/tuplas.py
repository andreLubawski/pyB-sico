"""print(type(()))

a = (1)
print(type(a))
# int

b = (4,)
print(type(b))

# tuplas são definidas por vírgula, e não por parênteses

tup = tuple(range(11))
print(tup)

tupla = ("andré", "lubawski")
nome, sobrenome = tupla
print(nome)
print(sobrenome)
"""
t1 = (1, 2, 3)
t2 = (3, 4, 5)
print(t1 + t2)

t1 = t1 + t2
print(t1)

print(t1.count(3))

print(t1.index(1))
