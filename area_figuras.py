#Exercício 01 (Área do Quadrado)

lado_quadrado = float(input("Digite o valor do lado do quadrado: "))
area_quadrado = lado_quadrado ** 2
print(f"A área do quadrado é: {area_quadrado:.2f} metros quadrados.")
print(f"A área do quadrado é: {area_quadrado * 10000:.2f} centímetros quadrados.")

#Exercício 02 (Área do Retângulo)

base_retangulo = float(input("Digite o valor da base do retângulo: "))
altura_retangulo = float(input("Digite o valor da altura do retângulo: "))
area_retangulo = base_retangulo * altura_retangulo
print(f"A área do retângulo é: {area_retangulo:.2f} metros quadrados.")
print(f"A área do retângulo é: {area_retangulo * 10000:.2f} centímetros quadrados.")

#Exercício 03 (Área do Círculo)
import math

raio_circulo = float(input("Digite o valor do raio do círculo: "))
area_circulo = math.pi * (raio_circulo ** 2)
print(f"A área do círculo é: {area_circulo:.2f} metros quadrados.")
print(f"A área do círculo é: {area_circulo * 10000:.2f} centímetros quadrados.")