class Carro:
    def __init__(self, marca = '', modelo = '', ano = 2000):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        
    @property
    def marca(self):
        return self._marca
    
    @marca.setter
    def marca(self, marca):
        self._marca = marca
        
    @property
    def modelo(self):
        return self._modelo
    
    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo
        
    @property
    def ano(self):
        return self._ano
    
    @ano.setter
    def ano(self, ano):
        self._ano = ano
        
siena = Carro('Fiat', 'Siena', 2016)
# siena.marca = 'Fiat'
# siena.modelo = 'Siena'
# siena.ano = 2016

print(siena.__dict__)