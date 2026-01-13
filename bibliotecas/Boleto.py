import date

#Classe usando lib externa
class Boleto:
    def __init__(self, name, codigo):
        self._name = name
        self._codigo = codigo
        self.dataGeracao = date.dateFormat()

    def generateBoleto(self):
        return str(self.__dict__)
    
boleto = Boleto('Notebook', '12345678910')
print(boleto.generateBoleto())