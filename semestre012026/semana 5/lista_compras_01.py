"""
########################################################
#####         Adicionar ítens no carrinho          #####
#####                 **********                   #####            
#####          Autor: Alexandre Peregrino          #####
########################################################

""" 

carrinho =[]
print()
print("Digite fim para encerrar a lista de compras! ")
print()
while True:
    item_compra = input("Informe o ítem: ")
    if item_compra.lower() == "fim":
        break
    carrinho.append(item_compra)

print()

print(f'A lista de compras é: {carrinho}')