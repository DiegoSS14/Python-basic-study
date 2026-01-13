class Jogador:
    def __init__(self, nome, qtdVitorias, qtdDerrotas):
        self.nome = nome
        self.qtdVitorias = qtdVitorias
        self.qtdDerrotas = qtdDerrotas

    def totalJogador(self):
        return self.qtdVitorias - self.qtdDerrotas        

    def __add__(self, other):
        return self.totalJogador() + other.totalJogador()
    
    def __gt__(self, other):
        jogadorSelf = self.totalJogador()
        jogadorOther = other.totalJogador()
        return jogadorSelf > jogadorOther

    def __lt__(self, other):
        jogadorSelf = self.totalJogador()
        jogadorOther = other.totalJogador()
        return jogadorSelf < jogadorOther
    
    def __str__(self):
        return str(self.__dict__)

jogador1 = Jogador('Pinguin', 20, 10)
jogador2 = Jogador('Orca', 30, 6)

print(jogador1 > jogador2)
print(jogador1 < jogador2)
print(jogador1)