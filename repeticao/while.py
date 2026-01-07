continuar = True

while continuar:

    tabuada = int(input("Tabuada de que? "))

    for i in range(1, 11):
        print(f"{tabuada} x {i} = {tabuada*i}")
        # for j in range(1, 11):
        #     print(f"{j} x {i} = {j*i}")

    continuar = input("Deseja continuar? (s/n)")
    continuar = True if continuar == "s" else False
