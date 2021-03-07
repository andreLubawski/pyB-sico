numero = input("Digite um número inteiro: ")

print("O nome digitado foi: " + numero)

print(type(numero))

# input recebe uma string por padrão, então, devo realizar um cast para garantir que é inteiro

numero2 = int(input("Digite outro número: "))
print(type(numero2))
print(numero2)