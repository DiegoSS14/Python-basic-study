class Ninja:
    def __init__(self, name, aldeia, elementoChakra, nivel):
        self.name = name
        self.aldeia = aldeia
        self.elementochakra = elementoChakra
        self.nivel = nivel
        
class Uchiha(Ninja):
    def __init__(self, name, aldeia, elementoChakra, nivel, sharingan = False, lider = False):
        super().__init__(name, aldeia, elementoChakra, nivel)
        self.name = name
        self.aldeia = aldeia
        self.elementoChakra = elementoChakra
        self.nivel = nivel
        self.sharingan = sharingan
        self.lider = lider
        
class Uzumaki(Ninja):
    def __init__(self, name, aldeia, elementoChakra, nivel, jutsuSelamento = 0):
        super().__init__(name, aldeia, elementoChakra, nivel)
        self.name = name
        self.aldeia = aldeia
        self.elementoChakra = elementoChakra
        self.nivel = nivel
        self.jutsuSelamento = jutsuSelamento
        
class Procurado:
    def __init__(self, recompensa, crimes):
        self.recompensa = recompensa
        self.crimes = crimes
        
class UchihaProcurado(Uchiha, Procurado):
    def __init__(self, name, aldeia, elementoChakra, nivel, sharingan=False, lider=False, recompensa = 100, crimes = 1):
        super().__init__(recompensa, crimes, elementoChakra, nivel)
        self.name = name
        self.aldeia = aldeia
        self.elementoChakra = elementoChakra
        self.nivel = nivel
        self.sharingan = sharingan
        self.lider = lider
        self.recompensa = recompensa
        self.crimes = crimes
        
ninja1 = UchihaProcurado('Itachi Uchiha', 'Aldeia da Folha', 'Fogo','Jonin', True, False, 800000, 200)
ninja2 = UchihaProcurado('Sasuke Uchiha', 'Aldeia da Folha', 'Raio', 'Genin', True, False, 200000, 30)

print(ninja1.__dict__)
print(ninja2.__dict__)