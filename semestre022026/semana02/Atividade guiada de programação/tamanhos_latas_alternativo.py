import csv
import math

def main():
    latas = ler_latas('volumes.csv')
    if not latas:
        return

    for lata in latas:
        lata['volume'] = calcular_volume(lata['raio'], lata['altura'])
        lata['area'] = calcular_area_superficie(lata['raio'], lata['altura'])
        lata['eficiencia'] = calcular_eficiencia_material(lata['volume'], lata['area'])
        lata['custo_por_volume'] = calcular_custo_por_volume(lata['custo'], lata['volume'])

    melhor_material = max(latas, key=lambda l: l['eficiencia'])
    melhor_preco = min(latas, key=lambda l: l['custo_por_volume'])

    print(f"{'Lata':<14} {'Volume':>10} {'Área':>10} {'V/A':>8} {'R$/cm³':>10}")
    print("-" * 56)
    for lata in latas:
        print(f"{lata['nome']:<14} {lata['volume']:>10.1f} {lata['area']:>10.1f} "
              f"{lata['eficiencia']:>8.2f} {lata['custo_por_volume']:>10.4f}")

    print()
    print(f"Mais eficiente em material: {melhor_material['nome']} "
          f"(V/A = {melhor_material['eficiencia']:.2f} cm)")
    print(f"Mais barata por volume: {melhor_preco['nome']} "
          f"(R$ {melhor_preco['custo_por_volume']:.4f}/cm³)")

def calcular_volume(raio, altura):
    """Volume do cilindro: V = pi * r² * h"""
    return math.pi * raio ** 2 * altura

def calcular_area_superficie(raio, altura):
    """Área total com as duas tampas: A = 2*pi*r*(h + r)"""
    return 2 * math.pi * raio * (altura + raio)

def calcular_eficiencia_material(volume, area):
    """Volume por cm² de material. Quanto maior, melhor."""
    return volume / area

def calcular_custo_por_volume(custo, volume):
    """Custo por cm³ armazenado. Quanto menor, melhor."""
    return custo / volume

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



if __name__ == '__main__':
    main()