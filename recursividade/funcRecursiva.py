
# Uma função que chama ela mesma em forma de loop se chama função recursiva
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

print(fatorial(10))