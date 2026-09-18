import math

numero_itens = int(input("Digite o número de itens: "))
quantidade_itens_por_caixa = int(input("Digite a quantidade de itens por caixa: "))

print(f"Para {numero_itens} itens, empacotando {quantidade_itens_por_caixa} itens por caixa, você precisará de {math.ceil(numero_itens / quantidade_itens_por_caixa)} caixas.")