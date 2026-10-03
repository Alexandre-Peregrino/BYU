def main():

    lista1 = ["vermelho", "laranja", "amarelo", "verde", "azul"]
    lista2 = ["vermelho", "laranja", "amarelo", "verde", "preto"]
    indice = comparar_listas(lista1, lista2)
    if indice == -1:
        print("O conteúdo das listas é igual")
    else:
        print(f"lista1 e lista2 diferem no índice {indice}")

def comparar_listas(lista1, lista2):

    # Pega tamanho das duas listas
    comprimento1 = len(lista1)
    comprimento2 = len(lista2)

    # Armazena o comprimento da menor lista
    limite = min(comprimento1, comprimento2)

    i = 0
    while i < limite:

        # Pega o elemento de mesmo índice de cada lista
        elemento1 = lista1[i]
        elemento2 = lista2[i]

        if elemento1  != elemento2: # Para o laço se encontrar elementos diferentes
            break
        i += 1 # Incementa o contador do laço

    if comprimento1 == comprimento2 == i: # Se os comprimentos forem iguais i = -1
        i = -1
    return i

if __name__ == "__main__":
    main()