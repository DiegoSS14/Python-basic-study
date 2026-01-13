class Cliente:
    # Atributo de classe (Só pode ser acessado através de um Class Method)
    emissor = 'SSPDF'

    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    @staticmethod
    def staticMethod():
        print('Call static method...')

    @classmethod
    def classMethod(cls):
        print(cls.emissor)

cliente2 = Cliente('João Santos', '000.000.000-00')
print(cliente2.__dict__)

Cliente.staticMethod()
Cliente.classMethod()