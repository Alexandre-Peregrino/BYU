
#iNSERINDO VÁRIOS ÍTENS NA LISTA

clientes = []
while True:
    nome_cliente = input('Qual o nome do cliente: ')
    if nome_cliente.lower() == "sair":
        break
    clientes.append(nome_cliente)
print(clientes)