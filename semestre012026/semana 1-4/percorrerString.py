# Percorrendo a string letra por letra

nome = "Alexandre"

# for letra in nome:
#     print(letra)

# print(nome[3]) # x
# print(nome[0:4])  # Alex
# print(nome[4:7])  # and
# print(nome[:4])  # Alex

# for i in range(len(nome)):
#     print(nome[i])

# Imprimindo índice e letra de uma palavra
# for i in range(len(nome)):
#     print(f"Índice: {i} - Letra: {nome[i]}")

for i, letra in enumerate(nome):
    print(f'Índice: {i} - letra {letra}')