# lista_compras.py

def imprimir(compras):
    for i in range(len(compras)):
        print(f'índice {i}, item {compras[i]}')
    return compras

# Só executa se rodar este arquivo diretamente
if __name__ == "__main__":
    compras = []

    while True:
        item_compra = input("Informe o ítem: ")
        if item_compra.lower() == "fim":
            break
        compras.append(item_compra)

    print()
    print(f'A lista de compras é: {compras}')
    print()

    remover_item = input('Qual ítem deseja remover? ')
    verifica = False
    for i in range(len(compras)):
        if remover_item.lower() == compras[i].lower():
            compras.pop(i)
            inserir_item = input('Qual ítem deseja inserir? ')
            compras.insert(i, inserir_item)
            verifica = True
            break
    if verifica:
        print(f'Sua nova lista é: {compras}')       
    else:
        print('Ítem não encontrado')

    print(imprimir(compras))