import math

def calcular_area_do_retangulo(base, altura):
    return base * altura

def calcular_area_do_quadrado(lado):
    return calcular_area_do_retangulo(lado, lado) # Ponto de encapsulamento: a função calcular_area_do_quadrado utiliza a função calcular_area_do_retangulo para calcular a área do quadrado, evitando duplicação de código.

def calcular_area_do_circulo(raio):
    return math.pi * raio ** 2

while True:
    opcao = input('Qual área deseja calcular? (1) Quadrado, (2) Retângulo, (3) Círculo, (sair) Encerrar: ').strip().lower()

    if opcao == 'sair':
        print('Encerrando o programa. Até logo!')
        break
    elif opcao == '1':
        lado = float(input('Informe o lado do quadrado: '))
        print(f'A área do quadrado é: {calcular_area_do_quadrado(lado):.2f}')
    elif opcao == '2':
        base = float(input('Informe a base do retângulo: '))
        altura = float(input('Informe a altura do retângulo: '))
        print(f'A área do retângulo é: {calcular_area_do_retangulo(base, altura):.2f}')
    elif opcao == '3':
        raio = float(input('Informe o raio do círculo: '))
        print(f'A área do círculo é: {calcular_area_do_circulo(raio):.2f}')
    else:
        print('Opção inválida. Digite 1, 2, 3 ou "sair".')