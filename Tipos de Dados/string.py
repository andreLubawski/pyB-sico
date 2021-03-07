# aspas simples, aspas duplas ,aspas simples(ou duplas) triplas

print('André' + ' Lubawski' + '\n##### ########')

nome = """abc
def """

print(nome)
print(nome.upper())
print(nome.lower())
print(nome.capitalize())

outroNome = "abc"

print(nome.split())
# transforma em uma lista de strings

print(nome[0:5])
print(nome.split()[1])

print(outroNome[::-1])
# inverte os elementos, .reverse() não pode ser usado em str
print(outroNome.replace('a', 'y'))
