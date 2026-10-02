# ============================================================
# Análise de dados de expectativa de vida
# Autor: Alexandre Peregrino
#
# Objetivo:
#   1. Carregar o conjunto de dados;
#   2. Percorrer os dados linha por linha, dividindo cada linha
#      em partes;
#   3. Encontrar o valor MAIS BAIXO e o valor MAIS ALTO de
#      expectativa de vida no conjunto de dados;
#   4. Exibir ambos os valores.
#
# Fonte de dados: expectativa-de-vida.csv
# Formato esperado de cada linha: pais,sigla,ano,expectativa
# ============================================================

with open('expectativa-de-vida.csv', encoding='utf-8') as dados_csv:

    next(dados_csv)  # pula a linha do cabeçalho

    # --- Inicialização dos acumuladores -----------------------
    # Padrão "None": significa "ainda não encontrei o primeiro
    # valor". O primeiro registro lido sempre entra na comparação.
    menor_expectativa = maior_expectativa = None
    pais_menor = pais_maior = ano_menor = ano_maior = None

    # --- Percorrimento do arquivo, linha por linha ------------
    for dados in dados_csv:
        dado_limpo = dados.strip().split(',')  # divide a linha em partes
        pais = dado_limpo[0].strip('"')
        ano = int(dado_limpo[2])
        expectativa = float(dado_limpo[3])  # valor numérico para comparar

        # Busca do valor MAIS BAIXO de expectativa de vida
        if menor_expectativa is None or expectativa < menor_expectativa:
            menor_expectativa = expectativa
            pais_menor = pais
            ano_menor = ano

        # Busca do valor MAIS ALTO de expectativa de vida
        if maior_expectativa is None or expectativa > maior_expectativa:
            maior_expectativa = expectativa
            pais_maior = pais
            ano_maior = ano

    # --- Resultados -------------------------------------------
    print(f'O valor mais baixo de expectativa de vida é: {menor_expectativa} de {pais_menor} em {ano_menor}')
    print(f'O valor mais alto de expectativa de vida é: {maior_expectativa} de {pais_maior} em {ano_maior}')