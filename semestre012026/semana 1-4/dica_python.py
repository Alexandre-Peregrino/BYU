def comparar_palavras(palpite, secreta):
    resultado = []
    for i, letra in enumerate(palpite):
        if letra == secreta[i]:
            resultado.append(letra.upper())
        elif letra in secreta:
            resultado.append(letra.lower())
        else:
            resultado.append('_')
    return ''.join(resultado)

def jogar():
    secreta = "PYTHON"  # palavra secreta
    tentativas = 0

    print("=== JOGO DA PALAVRA SECRETA ===")
    print(f"Dica: a palavra tem {len(secreta)} letras.\n")

    while True:
        palpite = input("Digite seu palpite: ").upper()
        tentativas += 1

        if len(palpite) != len(secreta):
            print(f"⚠️  A palavra tem {len(secreta)} letras. Tente novamente.\n")
            continue

        if palpite == secreta:
            print(f"\n🎉 ACERTOU! A palavra era {secreta}.")
            print(f"Tentativas: {tentativas}")
            break

        dica = comparar_palavras(palpite, secreta)
        print(f"Dica: {dica}\n")

jogar()