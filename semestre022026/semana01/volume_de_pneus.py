from datetime import datetime
from math import pi


# Melhoria do código de cálculo de volume de pneus,
# com adição de funcionalidade de compra e registro de contato em arquivo de log.



# Validação de dados de entrada
def entrada_dados(mensagem: str) -> float:
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Entrada inválida. Digite um número.")


# Lê os três valores e os devolve em uma tupla
def ler_itens() -> tuple[float, float, float]:
    largura = entrada_dados("Informe a largura do pneu (em mm): ")
    perfil = entrada_dados("Informe o perfil do pneu (em %): ")
    diametro = entrada_dados("Informe o diâmetro do pneu (em polegadas): ")
    return largura, perfil, diametro


# Cálculo do volume de um pneu em litros
def calcular_volume_pneu(largura: float, perfil: float, diametro: float) -> float:
    volume = (pi * largura ** 2 * perfil * (largura * perfil + 2540 * diametro)) / 10**10
    return volume


# Chamada, impressão das funções e escrita no arquivo de log
largura, perfil, diametro = ler_itens()

volume = calcular_volume_pneu(largura, perfil, diametro)

print(f"O volume aproximado é de {volume:.2f} litros")


# Captura da data e hora atual
data_atual = datetime.now().strftime("%Y-%m-%d")


print("")
resposta = input("Deseja comprar pneus com esse volume? (S/N): ").upper()

while resposta not in ["S", "N"]:
    print("Opção inválida. Digite 'S' para Sim ou 'N' para Não.")
    resposta = input("Deseja comprar pneus com esse volume? (S/N): ").upper()

contato = "Não fornecido"  # Valor padrão caso o usuário não queira fornecer o contato

if resposta == "S":
    print("Ótimo! Vamos prosseguir com a compra.")
    print("")
    contato = (input("Por favor, informe seu número de telefone para entrarmos em contato: "))
elif resposta == "N":
    print("Tudo bem! Se mudar de ideia, estamos à disposição.")


# Arquivo de log
with open("volumes.txt", "a") as arquivo:
    arquivo.write(f"{data_atual}, {largura:g}, {perfil:g}, {diametro:g}, {volume:.2f}, {contato}\n") 