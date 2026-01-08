print("Calculadora de divisão")


# n1 = int(input("Primeiro número: "))
# n2 = int(input("Segundo número: "))

# try:
#     print(f"resultado {n1 / n2}")
# except Exception as error:
#     print(f"Ocorreu um erro: {error}")

try:
    n1 = int(input("Primeiro número: "))
    n2 = int(input("Segundo número: "))
    print(f"resultado {n1 / n2}")
except ZeroDivisionError:
    print("Não é possível relizar divisão por zero!")
except ValueError:
    print("Não é possível realizar divisão a partir de letras!")
else:
    print("O programa foi executado corretamente.")
finally:
    print("End...")