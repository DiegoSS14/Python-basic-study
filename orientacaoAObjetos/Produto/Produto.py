class Produto:
    # ... # Ou "pass" para não precisar passar atributos

    # Construtor
    def __init__(self, marca, modelo, valor = 0, quantidade = 0 ):
        self.marca = marca
        self.modelo = modelo
        self.valor = valor
        self.quantidade = quantidade

    def comprar(self, quantidade):
        self.quantidade += quantidade

    def vender(self, quantidade):
        if quantidade > self.quantidade:
            print("Você não tem estoque suficiente!")
        else:
            self.quantidade -= quantidade

# Instâncias da classe produto
produto = Produto("Samsung", "Galaxy S25", 8700, 10)
produto.comprar(20)
produto.comprar(20)
produto.vender(100)

produto2 = Produto("Acer", "Acer Nitro v15", 5799, 20)
produto2.vender(10)

produto3 = Produto("LG", "G5", 6500, 20)
produto3.vender(20)

print(produto.__dict__)
print(produto2.__dict__)
print(produto3.__dict__)