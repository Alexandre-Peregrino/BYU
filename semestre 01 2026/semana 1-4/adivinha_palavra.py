# Jogo da adivinhação de palavras
# Autor: Alexandre Peregrino

#Criatividade:

# Usei as palavras reservadas True, continue e break para ajudar no trabalho do laço de repetição

#usei as funções len(), lower() e upper() para pegar o tamanho das strings e fazê-las maiúsculas e minúsculas

#Concatenei as strings com o operador += abreviado

#Uso de emogis e \n

palavra_secreta = "fidelidade"
tentativas = 0

print()
print("*" * 35)
print("* Jogo da Adivinhação de Palavras *")
print("*" * 35)
print()

while True:
    palpite = input(f"Qual a palavra secreta? ({len(palavra_secreta)} letras: {'_ ' * len(palavra_secreta)}): ").lower()
    tentativas += 1

    # 1. Verifica se acertou
    if palpite == palavra_secreta:
        print(f"\n🎉 ACERTOU! A palavra era {palavra_secreta.upper()}.")
        print(f"Tentativas: {tentativas}")
        break

    # 2. Verifica quantidade de letras
    if len(palpite) != len(palavra_secreta):
        print(f"A palavra tem {len(palavra_secreta)} letras. Tente novamente.\n")
        continue

    # 3. Monta a dica letra por letra
    dica = ""
    for i in range(len(palpite)):
        if palpite[i] == palavra_secreta[i]:
            dica += palpite[i].upper()   # maiúscula = letra certa na posição certa
        elif palpite[i] in palavra_secreta:
            dica += palpite[i].lower()   # minúscula = letra existe em outra posição
        else:
            dica += "_"                  # underline = letra não existe

    print(f"Dica: {dica}\n")