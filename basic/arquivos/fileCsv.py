import csv

cars = [
    ["Fiat", "Pálio", "2017"],
    ["VW", "Gol", "1999"],
    ["VW", "Virtus", "2002"],
]

with open("./arquivos/cars.csv", "w", newline="") as fileCsv:
    fileCsv = csv.writer(fileCsv, delimiter=";")

    fileCsv.writerow(['Marca', 'Modelo', 'Ano'])
    fileCsv.writerows(cars)