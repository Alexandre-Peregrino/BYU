def main():
    # Cria um dicionário que contém dados sobre seis veículos.
    # A chave de cada veículo é o número de identificação (chassi).
    # O valor associado a cada chave é uma lista com o ano, fabricante,
    # modelo, cor, tipo de motor e cilindrada.
    veiculos_dic = {
        # chassi: [ano, fabricante, modelo, cor, tipo_motor, cilindrada]
        "9BWZZZ377VT004251": [2015, "Volkswagen", "Gol", "prata", "1.6", 1.6],
        "9HGFC2670HR123456": [2020, "Honda", "Civic", "vermelho", "I4", 2.0],
        "93HFB2580FZ000456": [2018, "Chevrolet", "Onix", "preto", "1.0", 1.0],
        "93YCZ45A9KJ012789": [2017, "Fiat", "Uno", "branco", "1.0", 1.0],
        "8ADAE48A0K1111223": [2019, "Toyota", "Corolla", "cinza", "2.0", 2.0],
        "9BG116GW0LC123456": [2021, "Chevrolet", "S10", "azul", "2.8 diesel", 2.8]
    }
    ANO_VEICULO = 0
    FABRICANTE_INDICE = 1
    MODELO_INDICE = 2
    COR_INDICE = 3
    TIPO_MOTOR = 4
    CILINDRADA = 5

    # Solicita ao usuário que insira um número de identificação do veículo (chassi).
    chassi = input("Por favor, digite o chassi: ")

    # Verifica se o chassi é uma chave que está no dicionário de veículos.
    if chassi in veiculos_dic:

        # Encontra os dados do veículo que o usuário deseja.
        dados = veiculos_dic[chassi]
        ano, fabricante, modelo, cor, tipo, cilindrada = dados

        # Imprime o fabricante, o modelo e a cor do veículo.
        # Não imprime o ano, o tipo de motor ou a cilindrada.
        print(f"Fabricante: {fabricante}, Modelo: {modelo}, Cor: {cor}")
    else:
        # Imprime uma mensagem informando que o chassi inserido
        # pelo usuário não está no dicionário.
        print(f"{chassi} não está no dicionário.")


# Se este arquivo for executado assim:
# > python teach_solution.py
# então chama a função main. Porém, se este arquivo
# for apenas importado, pule a chamada da função main.
if __name__ == "__main__":
    main()

