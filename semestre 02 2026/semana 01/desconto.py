"""
Sistema de cálculo de compra com imposto e desconto promocional.

Regras de negócio:
- O usuário informa itens (valor e quantidade) até digitar 0 na quantidade.
- Imposto: 6% sobre o subtotal.
- Desconto: 10% sobre o subtotal, aplicado apenas quando o subtotal
  for >= 50 e o dia da semana for terça (1) ou quarta (2).
- Com desconto: total = (subtotal - desconto) + imposto.
- Sem desconto: total = subtotal + imposto.
- Em dias de promoção, se o subtotal for < 50, informa quanto falta
  para atingir o valor mínimo do desconto.
"""

from datetime import date

# Constantes de negócio
IMPOSTO_PERCENTUAL = 0.06
DESCONTO_PERCENTUAL = 0.10
VALOR_MINIMO_DESCONTO = 50.0
DIAS_PROMOCAO = (1, 2)  # 0=segunda, 1=terça, 2=quarta, ..., 6=domingo

# Validação de entrada (float). Lê um número do usuário, tratando entradas inválidas.
def ler_valor(mensagem: str) -> float:
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Entrada inválida. Digite um número.")

# Lê os itens da compra e retorna o subtotal acumulado.
def ler_itens() -> float:
    subtotal = 0.0
    while True:
        valor = ler_valor("Informe o valor do item: ")
        quantidade = ler_valor("Informe a quantidade de itens (0 para encerrar): ")
        if quantidade == 0:
            break
        if valor < 0 or quantidade < 0:
            print("Valores negativos não são permitidos.")
            continue
        subtotal += valor * quantidade
    return subtotal

# Calcula imposto, desconto e total conforme as regras de negócio.
def calcular_total(subtotal: float, dia: int) -> tuple[float, float, float]:
    imposto = subtotal * IMPOSTO_PERCENTUAL
    desconto = 0.0
    if subtotal >= VALOR_MINIMO_DESCONTO and dia in DIAS_PROMOCAO:
        desconto = subtotal * DESCONTO_PERCENTUAL
        total = (subtotal - desconto) + imposto
    else:
        total = subtotal + imposto
    return imposto, desconto, total

def main() -> None:
    """Fluxo principal do programa."""
    dia = date.today().weekday()
    subtotal = ler_itens()

    imposto, desconto, total = calcular_total(subtotal, dia)

    if desconto > 0:
        print(f"Seu desconto foi de: R$ {desconto:.2f}")
    print(f"O imposto foi: R$ {imposto:.2f}")
    print(f"Total: R$ {total:.2f}")

    if dia in DIAS_PROMOCAO and subtotal < VALOR_MINIMO_DESCONTO:
        falta = VALOR_MINIMO_DESCONTO - subtotal
        print(f"Faltam R$ {falta:.2f} para o desconto de 10%!")

if __name__ == "__main__":
    main()