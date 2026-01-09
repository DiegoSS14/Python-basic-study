file = open("./arquivos/file.txt", "w+")

file.write("Name: Diego Sousa\n")
file.write("Role: Designer\n")
file.write("Phone: (61) 9 9999-9999\n")

file.close()

with open("./arquivos/file.txt", "r") as fileRead:
    for line in fileRead:
        print(line)