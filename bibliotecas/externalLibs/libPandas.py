import pandas

pessoas = [
    {'id':'8485', 'name':'Diego Sousa', 'uf':'DF', 'faturamento':21224533,},
    {'id':'4564', 'name':'Carlos Amaral', 'uf':'PE', 'faturamento':1115521,},
    {'id':'5124', 'name':'Fernando Oliveira', 'uf':'MA', 'faturamento':664588,},
    {'id':'3213', 'name':'Maria Silvestre', 'uf':'AM', 'faturamento':24565,},
    {'id':'3547', 'name':'Carla Cruz', 'uf':'SP', 'faturamento':7755684533,},
]

dataFrame = pandas.DataFrame(pessoas)

dataOrder = dataFrame.sort_values(by='faturamento', ascending=False)

print(dataOrder.head(len(pessoas))['name'])