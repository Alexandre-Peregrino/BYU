def main():

    # Cria um dicionário com números de identificação dos estudantes como chaves
    # e dados dos estudantes armazenados em uma lista como valores.
    dic_de_estudantes = {
        "42-039-4736": ["Carlos", "Silva", "sil20001@byui.edu", 16],
        "61-315-0160": ["Maria", "Oliveira", "oli21002@byui.edu", 3],
        "10-450-1203": ["Ana", "Soares", "soa22005@byui.edu", 15],
        "75-421-2310": ["João", "Pereira", "per20003@byui.edu", 5],
        "07-103-5621": ["Maria", "Oliveira", "oli19008@byui.edu", 0],
        "81-298-9238": ["Samanta", "Pascal", "pas21004@byui.edu", 8]
    }

    # Estes são os índices dos elementos nas listas de valores.
    INDICE_DE_NOME = 0
    INDICE_DE_SOBRENOME = 1
    INDICE_DE_EMAIL = 2
    INDICE_DE_CREDITOS = 3
    total = 0

    # Para cada item da lista, adicione o número de créditos que o estudante obteve.
    for item in dic_de_estudantes.items():
        chave = item[0]
        valor = item[1]

        # Recupera o número de créditos da lista de valores.
        creditos = valor[INDICE_DE_CREDITOS]
        nome = valor[INDICE_DE_NOME]
        print(f"Estudante {chave}, {nome} tem {creditos} creditos")

        # Soma o número de créditos ao total.
        total += creditos
    print(f"Total de créditos obtidos por todos os estudantes é: {total}")
# Chama main para iniciar este programa.
if __name__ == "__main__":
    main()