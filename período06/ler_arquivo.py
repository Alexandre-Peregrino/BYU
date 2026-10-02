def main():
    lista_de_texto = lita_de_leitura("plantas.txt")
    print(lista_de_texto)

def lista_de_leitura():
    lista_de_texto = []
    with open(plantas.txt, "rt", encoding="utf-8") as arquivo_de_texto:
        for linha in arquivo_de_texto:
            linha_limpa = linha.strip()
            lista_de_texto.append(linha_limpa)
        return lista_de_texto
if __name__ == "__main__":
    main()
