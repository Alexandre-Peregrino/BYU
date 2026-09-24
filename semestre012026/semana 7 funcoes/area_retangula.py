def obter_numero_positivo(texto_prompt):

     while True:
        try:
            numero = float(input(texto_prompt))
            if numero > 0:
                return numero
            print("O número deve ser positivo. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número válido.")


comprimento = obter_numero_positivo("Informe o comprimento do retângulo: ")

largura = obter_numero_positivo("Informe a largura do retângulo: ")

area = comprimento * largura

print(f"A área do retângulo é: {area}")