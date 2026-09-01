def main():
    favorita = input('Qual sua letra favorita? ')
    palavra = 'inconstitucionalissimamente'
    verifica = False

    for i in palavra:
        if favorita == i:
            print(favorita.upper())
            verifica = True
        else:
            print(i)

    if not verifica:
        print('Não há letras coincidentes na palavra')
        return  # sai da função aqui - Requisito 2 e 3 não executam

    print()

    # Requisito 2
    for i in palavra:
        if favorita == i:
            print(favorita.upper(), end=' ')
        else:
            print(i, end=' ')
    print()


    # Requisito 3
    for i in palavra:
        if favorita == i:
            print('_', end=' ')
        else:
            print(i, end=' ')
    print()

main()