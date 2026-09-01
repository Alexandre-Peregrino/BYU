secreta = "fidelidade"
tentativas = 0

print("=== JOGO DA PALAVRA SECRETA ===")
print(f"Dica: a palavra tem {len(secreta)} letras.\n")

while True:
    palpite = input("Digite seu palpite: ").lower()
    tentativas += 1

    if len(palpite) != len(secreta):
        print(f"A palavra tem {len(secreta)} letras. Tente novamente.\n")
        continue

    if palpite == secreta:
        print(f"\nACERTOU! A palavra era {secreta}.")
        print(f"Tentativas: {tentativas}")
        break

    # Monta a dica letra por letra
    dica = ""
    for i in range(len(palpite)):
        if palpite[i] == secreta[i]:
            dica += palpite[i].upper()
        elif palpite[i] in secreta:
            dica += palpite[i].lower()
        else:
            dica += "_"

    print(f"Dica: {dica}\n")