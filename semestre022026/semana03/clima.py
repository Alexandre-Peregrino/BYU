def fahr_para_celsius(fahr):
    celsius = (fahr - 32) / 1.8
    return celsius


if __name__ == "__main__":
    # Converte a entrada do usuário de texto (str) para número decimal (float)
    teste = float(input("Digite o valor em fahr: "))
        
    resultado = fahr_para_celsius(teste)
    print(f"Temperatura em Celsius: {resultado:.2f}°C")