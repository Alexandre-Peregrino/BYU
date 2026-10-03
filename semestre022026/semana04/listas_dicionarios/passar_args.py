"""
Demonstra que números são passados para uma função por valor
e listas são passadas por referência.
"""

def main():
    print("main()")
    x = 5
    lx = [7, -2]
    print(f"    Antes de chamar modificar_args(): x {x}  lx {lx}")

    # Passa um número inteiro e uma lista para a função modificar_args.
    modificar_args(x, lx)

    print(f"    Após chamar modificar_args():  x {x}  lx {lx}")


def modificar_args(n, lista):
    """Demonstra que o computador passa um valor para inteiros e uma referência para listas.
    Parâmetros:
        n: Um número
        lista: Uma lista
    Retorno: nada
    """
    print("    modificar_args(n, lista)")
    print(f"Antes de alterar n e lista: n {n}  lista {lista}")

    # Altera os valores de ambos os parâmetros.
    n += 1
    lista.append(4)

    print(f"        Após alterar n e lista:  n {n}  lista {lista}")


# Se este arquivo for executado assim:
# > python passar_args.py
# então chama a função main. No entanto, se este arquivo
# for apenas importado, a chamada para main será ignorada.
if __name__ == "__main__":
    main()
