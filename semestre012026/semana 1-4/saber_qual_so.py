import os
import platform

def info_sistema():
    print(f'Sistema: {platform.system()}')    # Windows, Linux, Darwin
    print(f'Nome do SO: {os.name}')            # nt, posix
    print(f'Versão: {platform.release()}')     # 10, 11, 22.04...

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Uso:
limpar_tela()
info_sistema()


