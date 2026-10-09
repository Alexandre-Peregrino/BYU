# Contador de Frequência de Palavras
# Analisa um arquivo de texto e mostra as palavras mais frequentes.

import string  # módulo do Python que tem a lista de pontuações (, . ! ? etc.)


def ler_arquivo(nome_arquivo):
    """Recebe o nome do arquivo e retorna o texto completo como string."""
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        texto = arquivo.read()
    return texto


def normalizar_texto(texto):
    """Recebe o texto e retorna a versão em minúsculas, sem pontuação."""
    texto = texto.lower()
    com_espacos = ""
    for caractere in texto:
        if caractere in string.punctuation + "—–":
            com_espacos += " "   # pontuação vira espaço em vez de sumir
        else:
            com_espacos += caractere
    return " ".join(com_espacos.split())  # limpa espaços duplos


def contar_palavras(texto):
    """Recebe o texto normalizado e retorna {palavra: quantidade}."""
    contagem = {}
    palavras = texto.split()  # quebra o texto em lista de palavras
    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra] += 1   # palavra já existe: soma 1
        else:
            contagem[palavra] = 1    # primeira vez: começa em 1
    return contagem


def ordenar_contagem(contagem):
    """Recebe o dicionário e retorna a lista da mais frequente para a menos."""
    return sorted(contagem.items(), key=lambda item: item[1], reverse=True)


def main():
    nome_arquivo = input("Digite o nome do arquivo: ")
    texto = ler_arquivo(nome_arquivo)
    texto = normalizar_texto(texto)
    contagem = contar_palavras(texto)
    lista = ordenar_contagem(contagem)

    print("\nPalavras mais frequentes:")
    for palavra, quantidade in lista:
        print(f"{palavra}: {quantidade}")


if __name__ == "__main__":
    main()