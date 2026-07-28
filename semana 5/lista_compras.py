def imprimir(compras):
    for i, (item, precos) in enumerate(compras.items()):
        total_item = sum(precos)
        print(f'Índice {i}, item {item}, preços {precos}, total R$ {total_item:.2f}')

def remover(item_compra):
    for item in compras:
        if item.lower() == item_compra.lower():
            compras.pop(item)
            print(f'{item} foi removido')
            return True
    print('Item não encontrado')
    return False

if __name__ == "__main__":
    
    compras = {}

    while True:
        item = input("Informe o item (ou 'fim' para encerrar): ")
        if item.lower() == "fim":
            break
        preco = float(input("Informe o valor do item: "))
        
        if item in compras:
            compras[item].append(preco)
        else:
            compras[item] = [preco]

    # Depois de sair do loop de compras, pergunta sobre remover
    while True:
        print()
        print("Lista atual:")
        imprimir(compras)
        
        remover_item = input("Qual item deseja remover? (ou 'não' para sair): ")
        if remover_item.lower() == "não" or remover_item.lower() == "nao":
            break
        
        remover(remover_item)

    # Soma final
    print()
    print("=" * 30)
    print("RESUMO FINAL")
    print("=" * 30)
    total_geral = 0
    for item, precos in compras.items():
        total_item = sum(precos)
        total_geral += total_item
        print(f'{item}: R$ {total_item:.2f} ({len(precos)} compra(s))')
    print(f'TOTAL GERAL: R$ {total_geral:.2f}')