# Exemplo 8
def main():

    # Estes são os índices de cada elemento nas listas internas.
    INDICE_ANO_PLANTIO = 0
    INDICE_ALTURA = 1
    INDICE_CIRCUNFERENCIA = 2
    INDICE_QUANTIDADE_FRUTOS = 3

    # Cria uma lista composta que armazena listas internas.
    dados_macieiras = [

    #   [ano,  alt, circ, frutos]
        [2012, 2.7, 3.6,  70.5], #ind 0
        [2012, 2.4, 3.7,  81.3], #ind 1
        [2015, 2.3, 3.6,  62.7], #ind 2
        [2016, 2.1, 2.7,  42.1]  #ind 3
    ]

    alturas = []
    for altura in range(len(dados_macieiras)):
        alturas.append(dados_macieiras[altura][1])
    print (alturas)

    maior = 0
    for indice in range(len(alturas)):
        if alturas[indice] > maior:
            maior = alturas[indice]    

    print(f"A maior altura é {maior}")


    # Recupera uma lista interna da lista composta.
    uma_arvore = dados_macieiras[2]

    # Recupera um valor da lista interna.
    altura = uma_arvore[INDICE_ALTURA]

    # Exibe a altura da árvore.
    print(f"altura da árvore {3} é: {altura}")

# Chama main para iniciar este programa.
if __name__ == "__main__":
    main()