import math

def main():
  raio = float(input("Digite o raio de um cilindro: "))
  altura = float(input("Digite a altura de um cilindro: "))

  volume = calcular_volume_do_cilindro(raio, altura)

  print(f"Volume: {volume:.2f}")

def calcular_volume_do_cilindro(raio, altura): 
  volume = math.pi * raio**2 * altura
  return volume
main()