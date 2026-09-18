
# Programa para calcular o consumo de combustível em km/l e milhas por galão
def main():
    while True:
        try:
            inicial = float(input("Digite o km inicial: "))
            final = float(input("Digite o km final: "))
            quant_litros = float(input("Digite quantidade de litros consumidos: "))
        except ValueError:
            print("Erro: por favor, digite valores numéricos válidos.")
            continue
        if inicial < 0 or final < inicial or quant_litros <= 0:
            print("Erro: o km final não pode ser menor que o km inicial ou a quantidade de litros é inválida.")
            continue
        break

    # Calcula o consumo de combustível em km/l
    consumo = quilometros_por_litro(inicial, final, quant_litros)
    print(f"O consumo de combustível foi de {consumo:.2f} km/l")

    # Converte o consumo de combustível para milhas por galão
    milhas_por_galao = milhas_por_galao(consumo)
    print(f"O consumo de combustível foi de {milhas_por_galao:.2f} milhas/galão")


# Função para calcular o consumo de combustível em km/l
def quilometros_por_litro(inicial, final, quant_litros):
    return (final - inicial) / quant_litros

# Função para converter o consumo de combustível para milhas por galão
def milhas_por_galao(consumo_km_l):
    return consumo_km_l * 2.35215 

if __name__ == "__main__":
    main()