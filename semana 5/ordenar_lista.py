#Ordenar no braço

pontos = [34, 44,27,54, 48]

"""

for i in range(len(pontos)):
    for j in range(len(pontos)):
        if pontos[i] < pontos[j]:
            aux = pontos[i]
            pontos[i] = pontos[j]
            pontos[j] = aux
print(*pontos, sep=", ")

"""

#Ordenar com a função sort()

pontos.sort()
print(*pontos, sep=", ")
