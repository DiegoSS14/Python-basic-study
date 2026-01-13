class Categoria:
    def __init__(self, categoria):
        self._categoria = categoria
    
    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, categoria):
        self._categoria = categoria

    def __str__(self):
        return str(self.__dict__)



class Motorista:
    def __init__(self, name, cpf, categoria):
        self._name = name
        self._cpf = cpf
        self._categoria = categoria

    @property
    def categoria(self):
        return self._categoria
    
    @categoria.setter
    def categoria(self, categoria):
        self._categoria = categoria

    def __str__(self):
        return str({
            self._categoria.categoria,
            self._cpf,
            self._name,
        })

#Novo Motorista
categoria = Categoria('AB')
motorista = Motorista('Diego Sousa', '000.000.000-00', categoria)

print(motorista)