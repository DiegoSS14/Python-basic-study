class Produto:
    # ... # Ou "pass" para não precisar passar atributos

    # Construtor
    def __init__(self, marca, modelo, valor = 0, ):
        self.marca = marca
        self.modelo = modelo
        self.valor = valor

# Instâncias da classe produto
produto = Produto("Samsung", "Galaxy S25", 8700)
produto2 = Produto("Acer", "Acer Nitro v15", 5799)
produto3 = Produto("LG", "G5")

print(produto.__dict__)
print(produto2.__dict__)
print(produto3.__dict__)