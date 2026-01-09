
def somar(n1, n2):
    return n1 + n2

def subtrair(n1, n2):
    return n1 - n2

def multiplicar(n1, n2):
    return n1 * n2

def dividir(n1, n2):
    if(n2 == 0):
        print("Não é possível dividir por zero")
    else:
        return n1 / n2

# Função para calcular
def calcular(inputN1, inputN2, inputOperator):
    match inputOperator:
        case '+':
            return somar(inputN1, inputN2)
        case '-':
            return subtrair(inputN1, inputN2)
        case '*':
            return multiplicar(inputN1, inputN2)
        case '/':
            return dividir(inputN1, inputN2)
        case other:
            return 'Digite um operador válido, ou digite "end" para sair'

# Função para executar a lógica de tudo
def main():
    inputOperator = ''

    while inputOperator != 'end': 
        print() # Para pular uma linha
        inputN1 = int(input('Digite o primeiro número: '))
        inputN2 = int(input('Digite o segundo número: '))
        inputOperator = input('Digite o operador: ')
        calcular(inputN1, inputN2, inputOperator)

main()