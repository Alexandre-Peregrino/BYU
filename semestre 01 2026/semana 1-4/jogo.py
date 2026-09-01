# Jogo de Aventura
# Autor: Alexandre Peregrino

import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def jogo():
    limpar_tela()
    
    print("=" * 60)
    print("                    JOGO DE AVENTURA")
    print("=" * 60)
    print()
    print("Você acorda em um quarto escuro e misterioso.")
    print("Não há janelas, apenas três portas à sua frente:")
    print()
    print("  🚪  Porta 1    🚪  Porta 2    🚪  Porta 3")
    print()
    print("Apenas uma delas leva à saída.")
    print("As outras duas guardam destinos incertos")
    print("— e provavelmente nada agradáveis.")
    print("Escolha com sabedoria. Boa sorte!")
    print()
    print("-" * 60)

    while True:
        escolha = input("Digite o número da porta (1, 2 ou 3): ").strip()

        if escolha == "1":
            print()
            print("=" * 60)
            print("Você escolheu a porta 1, parabéns, você encontrou a saída! 🎉")
            print("=" * 60)
            break
        elif escolha == "2":
            print()
            print("=" * 60)
            print("Você escolheu a porta 2, você entrou no labirinto escuro")
            print("e se perdeu para sempre! 💀")
            print("=" * 60)
            break
        elif escolha == "3":
            print()
            print("=" * 60)
            print("Você escolheu a porta 3, você caiu em um abismo sem fim! 💀")
            print("=" * 60)
            break
        else:
            print("Opção inválida! Escolha 1, 2 ou 3.")

    print()
    print("-" * 60)
    print("                     FIM DE JOGO")
    print("-" * 60)

if __name__ == "__main__":
    jogo()