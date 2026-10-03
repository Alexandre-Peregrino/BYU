numeros = [1, 2, 3, 4, 5]
nomes = ['um', 'dois', 'três', 'quatro', 'cinco']

print("listas:")
print(numeros, nomes)

dict_numeros = dict(zip(numeros, nomes))

print("Dicionário")
print(dict_numeros)

numeros = list(dict_numeros.keys())
nomes = list(dict_numeros.values())

print(numeros, nomes)