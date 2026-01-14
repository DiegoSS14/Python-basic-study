import numpy as np

notas = [4, 3, 1, 5, 10, 9, 8, 10, 3, 2, 10]

notasNp = np.array(notas)
media = np.mean(notasNp) # calcula média do array

print(np.around(media)) # exibe e arredonda média