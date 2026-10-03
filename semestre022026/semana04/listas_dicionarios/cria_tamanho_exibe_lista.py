# Exemplo 1
def main():
    # Cria uma lista que contém cinco strings.
    cores = ["amarelo", "vermelho", "verde", "amarelo", "azul"]


    # Chama a função embutida len
    # e exibe o comprimento da lista.
    comprimento = len(cores)
    print(f"Número de elementos: {comprimento}")


    # Exibe o elemento que está armazenado
    # no índice 2 na lista de cores.
    print(cores[2])


    # Altera o elemento que está armazenado no
    # índice 3 de "amarelo" para "roxo".
    cores[3] = "roxo"


    # Exibe a lista de cores inteira.
    print(cores)

    
# Chama main para iniciar este programa.
if __name__ == "__main__":
    main()