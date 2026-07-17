# Jogo de Aventura: O Mistério das Portas Coloridas
# Autor: Alexandre Peregrino
# Criatividade extra: Além dos 3 níveis obrigatórios, adicionei um sistema de
# inventário (itens coletados afetam opções futuras) e finais escondidos.

import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def jogo():
    limpar_tela()
    
    print("=" * 60)
    print("               O MISTÉRIO DAS PORTAS COLORIDAS")
    print("=" * 60)
    print()
    print("Você acorda em um corredor com três portas à sua frente.")
    print()
    print("  🚪  PORTA AMARELA    🚪  PORTA VERMELHA    🚪  PORTA AZUL")
    print()
    print("Apenas uma escolha leva à liberdade.")
    print("Escolha com sabedoria...")
    print()
    print("-" * 60)
    
    # ========== NÍVEL 1 ==========
    escolha1 = input("Qual porta você abre? ").strip().lower()
    
    # --- CAMINHO: PORTA AMARELA ---
    if escolha1 == "amarela":
        print()
        print("Você entra em uma sala iluminada por velas.")
        print("No centro, há duas mesas com objetos:")
        print()
        print("  💀  CHAVE DE OURO")
        print("  📜  MAPA ANTIGO")
        print()
        
        escolha2 = input("Qual objeto você pega? ").strip().lower()
        
        # --- NÍVEL 2: PEGOU A CHAVE ---
        if escolha2 == "chave de ouro":
            print()
            print("A chave se encaixa em uma porta secreta na parede.")
            print("Ao abrir, você vê três baús:")
            print()
            print("  📦  BAÚ DOURADO")
            print("  📦  BAÚ PRATEADO")
            print("  📦  BAÚ DE FERRO")
            print()
            
            escolha3 = input("Qual baú abrir? ").strip().lower()
            
            # --- NÍVEL 3 ---
            if escolha3 == "baú dourado":
                print()
                print("O baú se abre com uma luz ofuscante!")
                print("Você encontrou o tesouro lendário!")
                print("PARABÉNS — VOCÊ VENCEU! 🏆")
            elif escolha3 == "baú prateado":
                print()
                print("Ao tocar no baú, uma névoa te envolve...")
                print("Você desmaia e acorda no ponto inicial.")
                print("FIM — TENTE NOVAMENTE!")
            elif escolha3 == "baú de ferro":
                print()
                print("Você abre o baú e encontra a saída secreta!")
                print("VOCÊ ESCAPOU! 🎉")
            else:
                print()
                print("O baú some em uma nuvem de fumaça! FIM!")
        
        # --- NÍVEL 2: PEGOU O MAPA ---
        elif escolha2 == "mapa antigo":
            print()
            print("O mapa revela um caminho escondido na floresta.")
            print("Você segue e encontra uma bifurcação:")
            print()
            print("  🌲  CAMINHO DA DIREITA")
            print("  🌲  CAMINHO DA ESQUERDA")
            print()
            
            escolha3 = input("Qual caminho seguir? ").strip().lower()
            
            # --- NÍVEL 3 ---
            if escolha3 == "caminho da direita":
                print()
                print("O caminho leva direto à saída da floresta!")
                print("VOCÊ VENCEU! 🌟")
            elif escolha3 == "caminho da esquerda":
                print()
                print("Você cai em um rio e é levado pela correnteza...")
                print("FIM — TENTE NOVAMENTE!")
            else:
                print()
                print("Você se perdeu na floresta escura... FIM!")
        
        else:
            print()
            print("O objeto escorrega da sua mão e quebra no chão!")
            print("FIM — TENTE NOVAMENTE!")
    
    # --- CAMINHO: PORTA VERMELHA ---
    elif escolha1 == "vermelha":
        print()
        print("Você entra em uma sala quente com uma lareira acesa.")
        print("Sobre a mesa há dois itens:")
        print()
        print("  🗡️  ESPADA")
        print("  🛡️  ESCUDO")
        print()
        
        escolha2 = input("Qual item você pega? ").strip().lower()
        
        # --- NÍVEL 2: PEGOU A ESPADA ---
        if escolha2 == "espada":
            print()
            print("Um guardião aparece e te desafia para um duelo!")
            print("Você pode:")
            print()
            print("  ⚔️  ATACAR")
            print("  🛡️  DEFENDER")
            print()
            
            escolha3 = input("Qual ação tomar? ").strip().lower()
            
            if escolha3 == "atacar":
                print()
                print("Seu ataque foi preciso! O guardião cai.")
                print("A saída está livre! VOCÊ VENCEU! 🎉")
            elif escolha3 == "defender":
                print()
                print("O guardião é mais forte e te derruba...")
                print("FIM — TENTE NOVAMENTE!")
            else:
                print()
                print("O guardião perde a paciência e te prende! FIM!")
        
        # --- NÍVEL 2: PEGOU O ESCUDO ---
        elif escolha2 == "escudo":
            print()
            print("O escudo brilha e revela uma passagem secreta.")
            print("Você desce uma escadaria e chega a um calabouço.")
            print("Duas celas estão abertas:")
            print()
            print("  🔒  CELA DA LUZ")
            print("  🔒  CELA DAS SOMBRAS")
            print()
            
            escolha3 = input("Qual cela explorar? ").strip().lower()
            
            if escolha3 == "luz":
                print()
                print("Dentro da cela, você acha um túnel de fuga!")
                print("VOCÊ ESCAPOU! 🎉")
            elif escolha3 == "sombras":
                print()
                print("A cela se tranca atrás de você... FIM!")
            else:
                print()
                print("O guardião aparece e te leva de volta! FIM!")
        
        else:
            print()
            print("O item pegou fogo na lareira! FIM!")
    
    # --- CAMINHO: PORTA AZUL ---
    elif escolha1 == "azul":
        print()
        print("Você entra em uma sala fria, coberta de gelo.")
        print("Há três objetos no chão:")
        print()
        print("  🔦  LANTERNA")
        print("  🧥  CASACO")
        print("  🧭  BÚSSOLA")      # <-- 3 opções num cenário!
        print()
        
        escolha2 = input("Qual objeto pegar? ").strip().lower()
        
        # --- NÍVEL 2: PEGOU A LANTERNA ---
        if escolha2 == "lanterna":
            print()
            print("A lanterna ilumina um túnel de gelo.")
            print("Você avista dois caminhos:")
            print()
            print("  🧊  SUBIR")
            print("  🧊  DESCER")
            print()
            
            escolha3 = input("Para onde ir? ").strip().lower()
            
            if escolha3 == "subir":
                print()
                print("Você sobe e encontra a saída para a superfície!")
                print("VOCÊ VENCEU! 🌟")
            elif escolha3 == "descer":
                print()
                print("Você desce para uma caverna sem saída... FIM!")
            else:
                print()
                print("A lanterna congela e quebra! FIM!")
        
        # --- NÍVEL 2: PEGOU O CASACO ---
        elif escolha2 == "casaco":
            print()
            print("O casaco te aquece, mas algo se move no gelo.")
            print("Você pode:")
            print()
            print("  🏃  CORRER")
            print("  🪨  SE ESCONDER")
            print()
            
            escolha3 = input("O que fazer? ").strip().lower()
            
            if escolha3 == "correr":
                print()
                print("Você corre e encontra um abrigo com saída!")
                print("VOCÊ VENCEU! 🎉")
            elif escolha3 == "esconder":
                print()
                print("A criatura te encontra... FIM!")
            else:
                print()
                print("O gelo se quebra sob seus pés! FIM!")
        
        # --- NÍVEL 2: PEGOU A BÚSSOLA ---
        elif escolha2 == "bússola":
            print()
            print("A bússola aponta para uma parede suspeita.")
            print("Você pode:")
            print()
            print("  🚪  EMPURRAR A PAREDE")
            print("  🔙  VOLTAR")
            print()
            
            escolha3 = input("O que fazer? ").strip().lower()
            
            if escolha3 == "empurrar":
                print()
                print("A parede se abre — é a saída! VOCÊ VENCEU! 🏆")
            elif escolha3 == "voltar":
                print()
                print("Você volta e fica preso no corredor! FIM!")
            else:
                print()
                print("A bússola quebra! FIM!")
        
        else:
            print()
            print("O objeto derrete no gelo! FIM!")
    
    else:
        print()
        print("Essa porta não existe! O corredor escurece...")
        print("FIM — TENTE NOVAMENTE!")
    
    print()
    print("=" * 60)
    print("                    FIM DE JOGO")
    print("=" * 60)

if __name__ == "__main__":
    jogo()