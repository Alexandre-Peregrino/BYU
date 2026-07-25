import random

numero = random.randint(1, 100)
continuar = 's'
while continuar == 's':
    print(f"{'*'*55}")
    print(f"{'*'*10} Bem-vindo ao jogo de adivinhação! {'*'*10}")
    print(f"{'*'*55}")
    print()

    palpite = int(input("Digite um número entre 1 e 100: "))
    contador = 1
    while palpite != numero:
        contador += 1
        if palpite < numero:
            print("O número é maior que o seu palpite.")
        elif palpite > numero:
            print("O número é menor que o seu palpite.")
        palpite = int(input("Digite outro número entre 1 e 100: "))
    print()
    print(f"Parabéns! Você acertou o número {numero} em {contador} tentativas.")
    print() 
    continuar = input("Deseja jogar novamente? (s/n): ")
print()
print("Obrigado por jogar! Até a próxima.")