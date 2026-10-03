# Exemplo 4
def main():

    # Cria um dicionário com listas como valores
    dic_de_estudantes = {

    # ID_do_estudante: [nome,    sobrenome,   e-mail,       créditos]
        "42-039-4736": ["Carlos", "Silva", "sil20001@byui.edu", 16],
        "61-315-0160": ["Maria", "Oliveira", "oli21002@byui.edu", 3],
        "10-450-1203": ["Ana", "Soares", "soa22005@byui.edu", 15],
        "75-421-2310": ["João", "Pereira", "per20003@byui.edu", 5],
        "07-103-5621": ["Maria", "Oliveira", "oli19008@byui.edu", 0]
    }

    # Índices dos elementos nas listas do dict_de_estudantes.
    INDICE_DE_NOME = 0
    INDICE_DE_SOBRENOME = 1
    INDICE_DE_EMAIL = 2
    INDICE_DE_CREDITOS = 3

    # Obtém um número de identificação de estudante do usuário.
    id = input("Digite um número de identificação de estudante: ")

    # Verifica se o número de identificação do estudante está no dicionário.
    if id in dic_de_estudantes:

        # Atribui a lista referente ao id do estudante à valor
        valor = dic_de_estudantes[id]

        # Extrai da lista o nome
        nome = valor[INDICE_DE_NOME]

        # Extrai da lista o sobrenome do estudante
        sobrenome = valor[INDICE_DE_SOBRENOME]

        # Exibe o nome e sobrenome do estudante.
        print(f"{nome} {sobrenome}")
    else:
        print("Estudante inexistente")
# Chama main para iniciar este programa.
if __name__ == "__main__":
    main()