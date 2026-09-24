"""
########################################################
#####   Programa para manipular listas numéricas   #####
#####                 **********                   #####                                         
#####          Autor: Alexandre Peregrino          #####
########################################################

""" 
# Função para ordenar a lista

def ordenar(lista):
    for i in range(len(lista)):
        for j in range(len(lista)):
            if lista[i] < lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return lista

# Declaração de variáveis

lista_numerica = []
soma = 0
cont = 0
media = 0
maior = None
menor = None

# Laço para popular a lista, calcular a soma e a média, pegar maior número e o menor número positivo

while True:
    numero = int(input("Informe qual o número: "))
    if numero == 0:
        break
    else:
        cont += 1
        lista_numerica.append(numero)
        soma += numero
        media = soma / cont
        if maior is None or numero > maior:
            maior = numero
        if numero > 0:
            if menor is None or menor > numero:
                menor = numero

# Função para imprimir as saídas, chamar a função ordenar e imprimí-la

print(f'lista: {lista_numerica},\nlista ordenada: {ordenar(lista_numerica)},\nsoma: {soma},\nmédia: {media},\nmaior: {maior},\nmenor positivo: {menor}')