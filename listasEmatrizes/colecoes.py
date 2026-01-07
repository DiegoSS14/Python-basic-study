# conjunto
conjunto = set([0, 1, 2, 3, 4])
print("Conjunto ", conjunto)

# tupla
tupla = (0, 1, 2, 3, 4)
print("tupla ", tupla)

# dicionário ou objeto
pessoa1 = {"nome": "Diego", "CPF": "0000-0000-00", "idade": 22}

pessoas = [
    pessoa1,
    {"nome": "Kellen", "CPF": "2222-2222-22", "idade": 23},
    {"nome": "Daniely", "CPF": "1111-1111-11", "idade": 18}
]

print()
print(pessoas)

print()
print(pessoas[1]['nome'])
