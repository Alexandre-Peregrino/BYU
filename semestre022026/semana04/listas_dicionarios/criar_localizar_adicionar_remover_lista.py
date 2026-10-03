# Exemplo 2
def main():
    # Cria uma lista vazia que conterá nomes de tecidos.
    tecidos = []


    # Adiciona três elementos no final da lista de tecidos.
    tecidos.append("veludo")
    tecidos.append("denim")
    tecidos.append("algodão fino")


    # Insere um elemento no início da lista de tecidos.
    tecidos.insert(0, "chiffon")
    print(tecidos)


    # Determina se algodão fino está na lista de tecidos.
    if "algodão fino" in tecidos:
        print("algodão fino está na lista.")
    else:
        print("algodão fino NÃO está na lista.")


    # Obtém o índice em que veludo está armazenado na lista de tecidos.
    i = tecidos.index("veludo")
    print(f"O índice de veludo é: {i}")


    # Substitui veludo por tafetá.
    tecidos[i] = "tafetá"
    print(f"Na posição {i} agora é: ", tecidos[i])


    # Remove o último elemento da lista de tecidos.
    tecidos.pop()
    print(tecidos)


    # Remove denim da lista de tecidos.
    tecidos.remove("denim")
    print("denim foi removido")


    # Obtém o comprimento da lista de tecidos e exibe-a.
    n = len(tecidos)
    print(f"A lista de tecidos agora contém {n} elementos.")
    print(tecidos)


# Chama main para iniciar este programa.
if __name__ == "__main__":
    main()
