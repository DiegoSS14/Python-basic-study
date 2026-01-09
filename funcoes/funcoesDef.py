
def dividir(n1, n2):
    if n2 == 0:
        print("Não é possível dividir por zero!")
        return
    return n1/n2 

def multiplicar(n1, n2):
    return n1 * n2

rMultiplicacao = multiplicar(20, 10)

print(f"Resultado da multiplicação é: {rMultiplicacao}")
print(f"Resultado da divisão: {dividir(100, 0)}")