# Adição criativa:

# Adição de cabeçalho para a calculadora, tornando o programa mais amigável e informativo.
# Comentários em cada etapa do código para explicar o que está sendo feito.
# Adicionar a entrada de outros custos, como bebidas e sobremesas, para tornar o cálculo mais completo.
# Adicionar a exibição do subtotal para crianças e adultos separadamente, além do subtotal geral.
# Função if para verificar se o valor recebido do cliente é suficiente para cobrir o total com imposto, e informar ao usuário caso não seja suficiente.

# Requisitos da etapa:

print("*" * 38)
print("* Calculadora de preços de refeições *")
print("*" * 38)

# Solicitar ao usuário os preços das refeições e a quantidade de pessoas

preco_crianca = float(input("Informe o preço da refeição da criança: "))

preco_adulto = float(input("Informe o preço da refeição do adulto: "))

qtd_criancas = int(input("Informe a quantidade de crianças: "))

qtd_adultos = int(input("Informe a quantidade de adultos: "))

outros_custos = float(input("Informe outros custos (como bebidas, sobremesas, etc.): ")) #Adicionando a entrada de outros custos

# Calcular o total para crianças, adultos e o total geral

total_criancas = preco_crianca * qtd_criancas
total_adultos = preco_adulto * qtd_adultos
total_geral = total_criancas + total_adultos + outros_custos

# Exibir os resultados

print(f"Subtotal para crianças: R$ {total_criancas:.2f}") #Adição do subtotal para crianças
print(f"Subtotal para adultos: R$ {total_adultos:.2f}") #Adição do subtotal para adultos
print(f"Subtotal geral: R$ {total_geral:.2f}")

# Requisitos finais:

# Solicitar ao usuário a taxa de imposto sobre o consumo

taxa = float(input("Informe a taxa de imposto sobre o consumo sem o símbolo de porcentagem (ex: 10 não 10%): "))
imposto = total_geral * (taxa / 100)

# Calcular o total com imposto e exibir o resultado final

total_com_imposto = total_geral + imposto
print(f"Imposto sobre o consumo: R$ {imposto:.2f}")
print(f"Total com imposto: R$ {total_com_imposto:.2f}")

# Calcular o troco e exibir o resultado

valor_recebido = float(input("Informe o valor recebido do cliente: "))

troco = valor_recebido - total_com_imposto

# Calcular o troco e exibir o resultado, considerando se o valor recebido é suficiente ou não

if troco < 0:
    print(f"O valor recebido é insuficiente. Faltam R$ {abs(troco):.2f} para completar o pagamento.")
else:
    print(f"O troco a ser devolvido ao cliente é: R$ {troco:.2f}")