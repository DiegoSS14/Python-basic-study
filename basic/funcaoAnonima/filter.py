numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numeros)

numerosNew = filter(lambda n: n % 2 == 0, numeros)
print(list(numerosNew))