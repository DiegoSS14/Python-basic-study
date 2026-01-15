import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Financa:
    def __init__(self, nome, valor, taxa, periodo):
        self.nome = nome
        self.valor = valor
        self.taxa = taxa
        self.periodo = periodo

investimentos = {
    'Investimentos1': Financa('Tesouro direto', 10000, 0.02, 5),
    'Investimentos2': Financa('Ações', 5000, 0.02, 2),
    'Investimentos3': Financa('Poupança', 3000, 0.02, 1),
    'Investimentos4': Financa('CDB', 20000, 0.02, 6),
}

l_investimentos = [i.__dict__ for i in investimentos.values()]

df_investimentos = pd.DataFrame.from_records(l_investimentos, index=investimentos.keys())
df_investimentos['Retornos'] = df_investimentos.apply(lambda l: l.valor * (1 + l.taxa) ** l.periodo, axis=1)

print(df_investimentos)

df_investimentos.plot(kind='bar', y='Retornos', legend='None')

plt.title('Retorno Investimentos')
plt.xlabel('Investimentos')
plt.ylabel('Retorno em reais')
plt.show()