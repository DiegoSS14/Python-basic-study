import matplotlib.pyplot as plt

class Campanha:
    def __init__(self, canal, investimento, cliques, conversao):
        self.canal = canal
        self.investimento = investimento
        self.cliques = cliques
        self.conversao = conversao

    def cpc(self):
        return self.investimento / self.cliques

campanhas = [
    Campanha('Facebook Ads', 5000, 2000, 320),
    Campanha('Instagram Ads', 5000, 2000, 320),
    Campanha('Email Ads', 5000, 2000, 320),
    Campanha('Google Ads', 5000, 2000, 320),
]

canais = [c.canal for c in campanhas]
cpcs = [c.cpc() for c in campanhas]

print(canais)
print(cpcs)

plt.bar(canais, cpcs)
plt.title('Custos por clique')
plt.xlabel('Canais')
plt.ylabel('Custo em real')
plt.show()