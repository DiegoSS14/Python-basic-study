numeros = [1, 2, 3, 4, 5]

print(numeros[0])

carros = ["Cruze", "Onix", "Corsa", "Virtus", "Camaro"]
print(carros)

carros.append('Kombi')
print(carros)

carros.remove('Onix')
print(carros)

del carros[0]
print(carros)

orderCarros = sorted(carros)
print(orderCarros)

for i in orderCarros:
    print(i)