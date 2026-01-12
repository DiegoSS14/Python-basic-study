from abc import ABC, abstractmethod

class Viagem(ABC):
    def __init__(self, valorKm, uf):
        self._valorKm = valorKm
        self._uf = uf
        
    @property
    def valorKm(self):
        return self._valorKm
    
    @property
    def uf(self):
        return self._uf
    
    @valorKm.setter
    def valorKm(self, valorKm):
        self._valorKm = valorKm
        
    @uf.setter
    def uf(self, uf):
        self._uf = uf
    
    @abstractmethod
    def calcularViagem(self):
        ...
        
class Nacional(Viagem):
    def __init__(self, valorKm = 1, uf = '', distancia = 2):
        super().__init__(valorKm, uf)
        self.distancia = distancia
    
    def calcularViagem(self):
        match self.uf:
            case 'DF':
                self.valorKm = 2.5
            case 'SP':
                self.valorKm = 2.2
            case 'AM':
                self.valorKm = 1.85
            case other:
                self.valorKm = 0.8
                
        return self.distancia * self.valorKm
    
viagem = Nacional(uf='MA', distancia=3000)
print(viagem.calcularViagem())