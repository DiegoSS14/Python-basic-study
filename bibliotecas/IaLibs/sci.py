from sklearn.cluster import KMeans
import numpy as np

class Produto:
    def __init__(self, nome, preco, peso):
        self.nome = nome
        self.preco = preco
        self.peso = peso

produtos = [
    Produto('Produto1', 1.99, 0.9),
    Produto('Produto2', 29.99, 0.9),
    Produto('Produto3', 35.5, 0.8),
    Produto('Produto4', 34.99, 0.2),
    Produto('Produto5', 20.99, 0.4),
    Produto('Produto6', 5.99, 0.3),
    Produto('Produto7', 4.99, 0.6),
    Produto('Produto8', 18.99, 0.8),
    Produto('Produto9', 160, 0.8),
    Produto('Produto10', 60.50, 0.8),
    Produto('Produto11', 60.50, 0.8),
    Produto('Produto12', 129.9, 0.8),
]

precos = [[p.preco, p.peso] for p in produtos]
matriz = np.array(precos)

kmeans = KMeans(n_init='auto', n_clusters=3, random_state=0).fit(matriz)
labels = kmeans.labels_

for i in range(3):
    print(f'grupo {i + 1}')
    for j in range(len(produtos)):
        if labels[j] == i:
            print(' - ', produtos[j].nome)