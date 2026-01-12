class Imovel:
    def __init__(self, name, uf, cep, value = ''):
        self.name = name
        self.uf = uf
        self.cep = cep
        self.value = value

class Residencial(Imovel):
    def __init__(self, name, uf, cep, value, piscina = False, quartos = 1, quintal = True):
        super().__init__(name, uf, cep, value = '')
        self.name = name
        self.uf = uf
        self.cep = cep
        self.value = value
        self.piscina = piscina
        self.quartos = quartos
        self.quintal = quintal

class Comercial(Imovel):
    def __init__(self, name, uf, cep, value, salas, andares, estacionamento):
        super().__init__(name, uf, cep, value = '')
        self.name = name
        self.uf = uf
        self.cep = cep
        self.value = value
        self.salas = salas
        self.andares = andares
        self.estacionamento = estacionamento
        
imovel = Imovel('Meu imóvel', 'DF', '75564844', 300000)
print(imovel.__dict__)

casa = Residencial('Minha casa', 'DF', '75564844', 300000, True, 3, True)
print(casa.__dict__)

empresa = Comercial('Dev Solutions', 'DF', '46236478', 1000000, 10, 3, True)
print(empresa.__dict__)