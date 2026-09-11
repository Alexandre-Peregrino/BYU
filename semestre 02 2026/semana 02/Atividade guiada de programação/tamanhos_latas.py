import csv
import math


def main():
    latas = ler_latas('volumes.csv')
    if not latas:
        return

    melhor_armazenamento = None
    melhor_custo = None

    # cabeçalho da tabela
    print(f"{'Lata':<14} {'Volume':>10} {'Área':>10} {'V/A':>8} {'Vol/R$':>10}")
    print("-" * 60)
    for lata in latas:

        # Volume recebe o valor retornado da função calcular_volume, que é chamada com os parâmetros raio e altura da lata.
        volume = calcular_volume(lata['raio'], lata['altura'])

        # Área recebe o valor retornado da função calcular_area_da_superficie, que é chamada com os parâmetros raio e altura da lata.
        area = calcular_area_da_superficie(lata['raio'], lata['altura'])

        # Eficiência de armazenamento recebe o valor retornado da função calcular_eficiencia_de_armazenamento, que é chamada com os parâmetros raio e altura da lata.
        efic_armazenamento = calcular_eficiencia_de_armazenamento(lata['raio'], lata['altura'])

        # Eficiência de custo recebe o valor retornado da função calcular_eficiencia_de_custo, que é chamada com os parâmetros raio, altura e custo da lata.
        efic_custo = calcular_eficiencia_de_custo(lata['raio'], lata['altura'], lata['custo'])

        # Desafio 4: if dentro do loop para achar os melhores automaticamente
        if melhor_armazenamento is None or efic_armazenamento > melhor_armazenamento[1]:
            melhor_armazenamento = (lata['nome'], efic_armazenamento)
            
        if melhor_custo is None or efic_custo > melhor_custo[1]:
            melhor_custo = (lata['nome'], efic_custo)

        print(f"{lata['nome']:<14} {volume:>10.1f} {area:>10.1f} "
              f"{efic_armazenamento:>8.2f} {efic_custo:>10.2f}")

    print()
    print(f"Melhor eficiência de armazenamento: {melhor_armazenamento[0]} "
          f"(V/A = {melhor_armazenamento[1]:.2f} cm)")
    print(f"Melhor eficiência de custo: {melhor_custo[0]} "
          f"(Vol/R$ = {melhor_custo[1]:.2f} cm³/R$)")


# Funções auxiliares
# Requisito 01
def calcular_volume(raio, altura):
    """Volume do cilindro: V = pi * r² * h"""
    return math.pi * raio ** 2 * altura

# Requisito 02
def calcular_area_da_superficie(raio, altura):
    """Área total com as duas tampas: A = 2*pi*r*(h + r)"""
    return 2 * math.pi * raio * (altura + raio)

# Requisito 03 (Desafio adicional 01)
def calcular_eficiencia_de_armazenamento(raio, altura):
    """Eficiência de armazenamento: volume / área. Quanto maior, melhor."""
    volume = calcular_volume(raio, altura)
    area = calcular_area_da_superficie(raio, altura)
    return volume / area


# (Desafio adicional 02)
def calcular_eficiencia_de_custo(raio, altura, custo):
    """Eficiência de custo: volume / custo. Quanto maior, melhor."""
    volume = calcular_volume(raio, altura)
    return volume / custo


def ler_latas(arquivo):
    """Lê o CSV e devolve uma lista de dicionários com valores numéricos."""
    latas = []
    try:
        with open(arquivo, mode='r', encoding='utf-8') as f:
            leitor = csv.DictReader(f)
            for linha in leitor:
                latas.append({
                    'nome': linha['Nome'],
                    'raio': float(linha['Raio']),
                    'altura': float(linha['Altura']),
                    'custo': float(linha['Custo']),
                })
    except FileNotFoundError:
        print(f"Erro: arquivo '{arquivo}' não encontrado.")
        return []
    except (ValueError, KeyError) as e:
        print(f"Erro: CSV mal formatado ({e}).")
        return []
    return latas


# Inicia este programa chamando a função main.
if __name__ == '__main__':
    main()