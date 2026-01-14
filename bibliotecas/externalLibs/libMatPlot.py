import matplotlib.pyplot as plt

# Gráfico de linhas
# meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
# valores = [100, 200, 300, 150, 100, 200, 350, 300, 280, 200, 300, 100]
# valores2 = [50, 80, 100, 150, 180, 220, 250, 280, 300, 350, 380, 385]

# plt.plot(meses, valores, label='Design', marker=".")
# plt.plot(meses, valores2, label='TI', marker=".")
# plt.xlabel('Meses')
# plt.ylabel('Valores')
# plt.title('Demandas atendidas')
# plt.legend()
# plt.show()

# Gráfico de barras
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
valores = [100, 200, 300, 150, 100, 200, 350, 300, 280, 200, 300, 100]
valores2 = [50, 80, 100, 150, 180, 220, 250, 280, 300, 350, 380, 385]

plt.bar(meses, valores, label='Design')
plt.bar(meses, valores2, label='TI')
plt.xlabel('Meses')
plt.ylabel('Valores')
plt.title('Demandas atendidas')
plt.legend()
plt.show()


# Gráfico de pizza
# navegadores = ['Chrome', 'Edge', 'OperaGx']
# valores = [5006, 500, 5824]
# colors = ['orange', 'blue', 'red']

# plt.pie(valores, labels=navegadores, colors=colors)
# plt.show()