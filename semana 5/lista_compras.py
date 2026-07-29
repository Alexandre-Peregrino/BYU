"""
########################################################
#####         Adicionar ítens no carrinho          #####
#####                 **********                   #####
#####          Autor: Alexandre Peregrino          #####
########################################################

##############################
#########CRIATIVIDADE#########
##############################

# Estratégias aplicadas para tornar o código mais eficiente e legível:
# - Funções para evitar repetição de código (DRY)
# - Dicionário para associar itens a listas de preços
# - enumerate para exibir índices começando em 1
# - list(compras.keys()) para acessar itens por posição
# - sum() aninhado para totalizar preços
# - try/except para validar entrada numérica e valores positivos
# - replace para tratar "." e "," modelo aceito pelo python
# - Subtotal exibido a cada inserção para auxiliar na tomada de decisão
"""

def imprimir(lista_compras):
    for i, (item, precos) in enumerate(lista_compras.items()):
        total_item = sum(precos)
        print(f'Índice {i + 1}, item {item}, preços {precos}, total R$ {total_item:.2f}')

def remover_por_indice(indice_exibido):
    itens = list(compras.keys())
    indice_zero = indice_exibido - 1

    if 0 <= indice_zero < len(itens):
        item_removido = itens[indice_zero]
        compras.pop(item_removido)
        print(f'{item_removido} foi removido')
        return True
    else:
        print('Índice inválido')
        return False

def calcular_soma(compras):
    return sum(sum(precos) for precos in compras.values())

# Loop para adicionar produtos às compras
compras = {}

while True:
    item = input("Informe o item (ou 'fim' para encerrar): ").lower()
    if item == "fim":
        break

    while True:
        try:
            preco = float(input("Informe o valor do item: ").replace(",", "."))
            if preco <= 0:
                print("O valor deve ser maior que zero. Tente novamente.")
            else:
                break
        except ValueError:
            print("Valor inválido. Digite um número.")

    if item in compras:
        compras[item].append(preco)
    else:
        compras[item] = [preco]

print()
subtotal = calcular_soma(compras)
print(f'Subtotal: R$ {subtotal:.2f}')
print()

# Loop para remover itens pelo índice
while True:
    print()
    print("Lista atual:")
    imprimir(compras)
    print()

    try:
        entrada = input("Digite o ÍNDICE do item para remover (ou 'não' para sair): ")
        if entrada.lower() in ("não", "nao"):
            break

        indice = int(entrada)
        remover_por_indice(indice)

    except ValueError:
        print("Digite um número válido.")

# Resumo final
print()
print("=" * 30)
print("RESUMO FINAL")
print("=" * 30)
imprimir(compras)

total_geral = calcular_soma(compras)
print(f'TOTAL GERAL: R$ {total_geral:.2f}')