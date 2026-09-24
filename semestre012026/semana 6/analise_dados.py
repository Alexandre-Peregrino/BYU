# ============================================================
# Análise de dados de expectativa de vida
# Autor: Alexandre Peregrino
#
# Objetivo:
#   1. Encontrar o país com a MAIOR e a MENOR expectativa de
#      vida em todo o arquivo (geral);
#   2. Para um ano escolhido pelo usuário, calcular a média,
#      a máxima e a mínima da expectativa de vida entre todos
#      os países daquele ano;

# --- (Demonstrando Criatividade e Indo Além dos Requisitos) ---

#   3. Para um país escolhido pelo usuário, calcular a média,
#      a máxima e a mínima da expectativa de vida em todos
#      os anos disponíveis. 
# Fonte de dados: expectativa-de-vida.csv
# Formato esperado de cada linha: pais,sigla,ano,expectativa
# ============================================================

with open('expectativa-de-vida.csv', encoding='utf-8') as dados_csv:

    next(dados_csv)  # pula a linha do cabeçalho

    # --- Inicialização dos acumuladores -----------------------
    # Padrão "None": significa "ainda não encontrei o primeiro
    # valor". O primeiro registro lido sempre entra na comparação,
    # sem depender de chutes como 0 ou 1.000.000.000.000.
    menor_expectativa = maior_expectativa = None
    pais_menor = pais_maior = ano_menor = ano_maior = None

    # Acumuladores de comparação do ano escolhido (mesmo padrão None)
    expectativa_maior_pais_ano = expectativa_menor_pais_ano = None
    pais_menor_expectativa = pais_maior_expectativa = None

    # Acumuladores de SOMA: começam em 0 (somar e contar)
    cont = 0
    expectativa_ano_escolhido = 0

    menor_pais = maior_pais = None
    cont_pais = soma_pais = 0

    # --- Validação do ano escolhido --------------------------
    # O laço "while True" só termina com "break", que acontece
    # quando o usuário digita um número inteiro positivo.
    while True:
        try:
            ano_escolhido = int(input("Informe o ano para análise: ").strip())
            if ano_escolhido > 0:
                break
            else:
                print('Informe um valor positivo.')
        except ValueError:
            print("Valor inválido. Digite um ano (inteiro), ex.: 1959.")

    # --- Validação do país escolhido ----------------------------
    # O laço "while True" só termina com "break", que acontece
    # quando o usuário digita algum valor de string válido, 
    # não pode ser vazio.
    while True:
        pais_escolhido = input("informe o país para análise: ").strip()
        if pais_escolhido:
            break
        print("O país não pode ser vazio. Digite um nome válido.")



    # --- Percorrimento do arquivo, linha por linha ------------
    for dados in dados_csv:
        dado_limpo = dados.strip().split(',')
        pais = dado_limpo[0].strip('"')
        ano = int(dado_limpo[2])          # int: comparação com ano_escolhido
                                          # exige o MESMO tipo
        expectativa = float(dado_limpo[3])  # float: maior/menor numéricos,
                                            # nunca comparação de texto

        # Busca da MENOR expectativa geral (todos os anos)
        if menor_expectativa is None or expectativa < menor_expectativa:
            menor_expectativa = expectativa
            pais_menor = pais
            ano_menor = ano

        # Busca da MAIOR expectativa geral (todos os anos)
        if maior_expectativa is None or expectativa > maior_expectativa:
            maior_expectativa = expectativa
            pais_maior = pais
            ano_maior = ano

        # Estatísticas do ano escolhido pelo usuário
        if ano_escolhido == ano:
            cont += 1                          # conta os países do ano
            expectativa_ano_escolhido += expectativa  # soma as expectativas

            # Maior expectativa dentro do ano escolhido
            if expectativa_maior_pais_ano is None or expectativa > expectativa_maior_pais_ano:
                pais_maior_expectativa = pais
                expectativa_maior_pais_ano = expectativa

            # Menor expectativa dentro do ano escolhido
            if expectativa_menor_pais_ano is None or expectativa < expectativa_menor_pais_ano:
                pais_menor_expectativa = pais
                expectativa_menor_pais_ano = expectativa

        #Estatísticas do país escolhido pelo usuário
        if pais_escolhido.lower() == pais.lower():
            cont_pais += 1
            soma_pais += expectativa
            if menor_pais is None or expectativa < menor_pais:
                menor_pais = expectativa
            if maior_pais is None or expectativa > maior_pais:
                maior_pais = expectativa

    # --- Resultados gerais (independentes do ano escolhido) ---
    print(f'A expectativa de vida máxima geral é: {maior_expectativa} de {pais_maior} em {ano_maior}')
    print(f'A expectativa de vida mínima geral é: {menor_expectativa} de {pais_menor} em {ano_menor}')

    # --- Resultados do ano escolhido --------------------------
    # A média é calculada UMA única vez, depois do laço
    # (regra: acumular dentro, resultado fora)
    if cont > 0:
        media_ano_escolhido = expectativa_ano_escolhido / cont
        print(f'Para o ano de {ano_escolhido}:')
        print(f'A média da expectativa de vida em todos os países era de {media_ano_escolhido:.2f} anos')
        print(f'A expectativa de vida máxima estava em {pais_maior_expectativa}, com {expectativa_maior_pais_ano:.2f} anos.')
        print(f'A expectativa de vida mínima estava em {pais_menor_expectativa}, com {expectativa_menor_pais_ano:.2f} anos.')
    else:
        print(f'Não há dados para o ano {ano_escolhido}.')

    # --- Resultados do país escolhido -------------------------
    # A média é calculada UMA única vez, depois do laço
    # (regra: acumular dentro, resultado fora)
    if cont_pais > 0:
        media_pais = soma_pais / cont_pais
        print(f'{pais_escolhido.title()}: mínima {menor_pais:.2f}, máxima {maior_pais:.2f}, média {media_pais:.2f}')
    else:
        print(f'País "{pais_escolhido}" não encontrado.')