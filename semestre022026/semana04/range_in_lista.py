# Exemplo 4
def main():
    # Conta de zero a nove de um em um.
    for i in range(10):
        print(i, end=" ")
    print()


    # Conta de cinco a nove de um em um.
    for i in range(5, 10):
        print(i, end=" ")
    print()


    # Conta de zero a oito de dois em dois.
    for i in range(0, 10, 2):
        print(i, end=" ")
    print()


    # Conta de 100 a 70 de três em três.
    for i in range(100, 69, -3):
        print(i, end=" ")
    print()

    # Cria uma lista de nomes de cores.
    cores = ["vermelho", "laranja", "amarelo", "verde", "azul"]


    # Usa um loop for para exibir cada elemento na lista.
    for cor in cores:
        print(cor, end=" ")
    print()


    # Usa um loop for diferente para
    # exibir cada elemento na lista.
    for i in range(len(cores)):
        # Usa o índice i para recuperar
        # um elemento da lista.
        cor = cores[i]
        print(cor, end=" ")

# Chama main para iniciar este programa.
if __name__ == "__main__":
    main()