from math import sqrt
# def raiz_quadrada(numero): 
#     return sqrt(numero)  

# resultado = float(input("Digite um número para calcular a raiz quadrada: "))
# raiz_quadrada(resultado)
# print(f"A raiz quadrada de {resultado} é {raiz_quadrada(resultado)}")

# def valor_absoluto(numero):
#     if numero < 0:
#         return -numero
#     else: 
#         return numero

# resultado = float(input("informe o número: "))
# valor_absoluto(resultado)
# print(f"O valor absoluto de {resultado} é {valor_absoluto(resultado)}")

def valor_positivo(numero):
    while True:
        if numero < 0:
            print("Número inválido. Digite um número positivo.")
            numero = float(input("Informe um número positivo: "))
        else:
            return numero

largura = float(input("Informe a largura: "))
largura = valor_positivo(largura)
comprimento = float(input("Informe o comprimento: "))
comprimento = valor_positivo(comprimento)
area = largura * comprimento
print(f"A área do retângulo é: {area}")