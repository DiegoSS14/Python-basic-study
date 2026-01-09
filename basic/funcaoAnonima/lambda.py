# numeros = [1, 2, 3, 4]

# resultado = []

# for n1 in numeros:
#     resultado.append(n1 * 2)


# print(numeros)
# print(resultado)

numeros = [2, 3, 4, 5, 6]
print(numeros)

# Usando lambda
numerosNew = map(lambda n: n*2, numeros)
print(list(numerosNew))