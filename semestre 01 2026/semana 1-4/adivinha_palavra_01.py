# Jogo da adivinhação de palavras
# Autor: Alexandre Peregrino

palavra_secreta = "fidelidade"
tentativas = 0

print()
print("*" * 35)
print("* Jogo da Adivinhação de Palavras *")
print("*" * 35)
print()

while True:
    palpite = input(f"Qual a palavra secreta? ({len(palavra_secreta)} letras): ").lower()
    tentativas += 1

    # 1. Verifica se acertou
    if palpite == palavra_secreta:
        print(f"\n🎉 ACERTOU! A palavra era {palavra_secreta.upper()}.")
        print(f"Tentativas: {tentativas}")
        break

    
   