n1 = 5
n2 = 2
n3 = 7
n4 = 3
n5 = 9
n6 = 8

soma = n1 + n2 + n3 + n4 + n5 + n6
media = soma / 6

if(media < 5) :
    print(f"Reprovado com média de {media} pts")
elif media >= 5 and media <= 6 :
    print(f"Em recuperação com média de {media} pts")
else: 
    print(f"Aprovado com média de {media} pts")