def main():
    lista_provincias = ler_lista("provincias.txt")
    # 3. Exibir a lista inteira
    print(lista_provincias)

    # 4. Remover o primeiro elemento
    lista_provincias.pop(0)

    # 5. Remover o último elemento
    lista_provincias.pop()

    # 6. Substituir todas as ocorrências de "AB" por "Alberta"
    for i in range(len(lista_provincias)):
        if lista_provincias[i] == 'AB':
            lista_provincias[i] = 'Alberta'
    print()
    # 7. Contar e exibir o número de "Alberta"
    print(f'Alberta aparece {lista_provincias.count('Alberta')} vezes na lista modificada')

def ler_lista(arquivo):
    lista_pronta =[]
    with open(arquivo, "rt", encoding="utf-8") as arquivo_provincias:
        lista_pronta = []
        for linha in arquivo_provincias:
            lista_pronta.append(linha.strip())
    return lista_pronta
    
if __name__ == "__main__":
    main()