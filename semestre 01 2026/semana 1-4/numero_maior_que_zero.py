numero = -1;

while numero < 0:
    try:
        numero = int(input("Digite um número positivo: "))
        if numero < 0:
            print("O número deve ser positivo. Tente novamente.")
    except ValueError:
        print("Entrada inválida! Por favor, digite um número inteiro.")

print (f"Você digitiou {numero}, que não é negativo. Obrigado!")