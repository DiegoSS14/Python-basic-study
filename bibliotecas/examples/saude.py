import pandas as pd
import numpy as np

class Pessoa:
    def __init__(self, nome, peso, altura):
        self.nome = nome
        self.peso = peso
        self.altura = altura


pacientes = {
    'pessoa1': Pessoa('Antonio', 85, 1.88), 
    'pessoa2': Pessoa('Maria', 90, 1.60),
    'pessoa3': Pessoa('Fernando', 60, 1.55),
    'pessoa4': Pessoa('Cácio', 68, 1.65),
    'pessoa5': Pessoa('Lúcia', 100, 1.85),
}

l_pacientes = [p.__dict__ for p in pacientes.values()]

df_pacientes = pd.DataFrame().from_records(l_pacientes, index=pacientes.keys())

df_pacientes['IMC'] = df_pacientes.apply(lambda i: i.peso / i.altura ** 2, axis=1)

media = np.mean(df_pacientes['IMC'])

sobrepeso = df_pacientes[df_pacientes['IMC'] > 25]

percentual = len(sobrepeso) / len(df_pacientes) * 100

print(df_pacientes)
print(media)
print(f'Pessoas com sobrepeso:\n{sobrepeso}')
print(f'Sobrepeso de {percentual}%')