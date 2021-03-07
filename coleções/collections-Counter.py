from collections import Counter

'''lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 2, 3, 4, 5, 5, 4]

resultado = Counter(lista)

print(type(resultado))
print(resultado)
# elemento: ocorrências
'''

# print(Counter('André Lubawski'))

texto = """
Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.
It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently 
with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
"""
palavras = texto.split()
print(Counter(palavras))
print(Counter(palavras).most_common(3))
