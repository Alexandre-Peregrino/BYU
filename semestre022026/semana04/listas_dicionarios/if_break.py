# Exemplo 6
def main():
    sum = 0

    # Obtém ao menos dez números do usuário e soma-os.
    for i in range(10):
        numero = float(input("Por favor, digite um número: "))
        if numero == 0:
            break
        sum += numero
    # Exibe a soma dos números para o usuário.
    print(f"soma: {sum}", end=" ")


# Chama main para iniciar este programa.
if __name__ == "__main__":
    main()