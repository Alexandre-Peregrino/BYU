# inserindo_varios_itens.py

def captura_clientes():
    clientes = []
    while True:
        nome_cliente = input('Qual o nome do cliente: ')
        if nome_cliente.lower() == "sair":
            break
        clientes.append(nome_cliente)
    return clientes

# Teste ao rodar o arquivo diretamente
if __name__ == "__main__":
    lista = captura_clientes()
    print(lista)