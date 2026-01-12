from abc import ABC, abstractmethod

class Ninja(ABC):
    def __init__(self, name, aldeia, elementoChakra, nivel):
        self.name = name
        self.aldeia = aldeia
        self.elementochakra = elementoChakra
        self.nivel = nivel
    
    @abstractmethod
    def throwJutsu(self, jutsu):
        ...
        
class Uchiha(Ninja):
    def __init__(self, name, aldeia, elementoChakra, nivel, sharingan = False, lider = False):
        super().__init__(name, aldeia, elementoChakra, nivel)
        self.name = name
        self.aldeia = aldeia
        self.elementoChakra = elementoChakra
        self.nivel = nivel
        self.sharingan = sharingan
        self.lider = lider
        
    def throwJutsu(self, jutsu, gasto, dano):
        return f'{jutsu}!!, Você gastou {gasto}% do seu chakra. Dano esperado de {dano}%'
        
class Procurado:
    def __init__(self, recompensa, crimes):
        self.recompensa = recompensa
        self.crimes = crimes
        
class UchihaProcurado(Uchiha, Procurado):
    def __init__(self, name, aldeia, elementoChakra, nivel, sharingan=False, lider=False, recompensa = 100, crimes = 1):
        Uchiha.__init__(self, name, aldeia, elementoChakra, nivel, sharingan, lider)
        Procurado.__init__(self, recompensa, crimes)
        self.recompensa = recompensa
        self.crimes = crimes

ninja2 = UchihaProcurado('Sasuke Uchiha', 'Aldeia da Folha', 'Raio', 'Genin', True, False, 200000, 30)
print(ninja2.__dict__)
print(ninja2.throwJutsu('Chidori', 20, 10))
