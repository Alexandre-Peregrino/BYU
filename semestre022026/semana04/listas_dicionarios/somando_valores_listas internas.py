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

    quantidade_total_de_frutos = 0
    for lista_interna in dados_macieiras:
        quantidade_de_frutos = lista_interna[INDICE_QUANTIDADE_FRUTOS]
        print(quantidade_de_frutos)
        quantidade_total_de_frutos += quantidade_de_frutos
    print(f"A quantidade total de de frutos é: {quantidade_total_de_frutos:.2f}")

# Chama main para iniciar este programa.
if __name__ == "__main__":
    main()