# Copyright 2020, Universidade Brigham Young-Idaho. Todos os direitos reservados.

from numeros_aleatorios import anexar_numeros_aleatorios
# from random_numbers import anexar_palavras_aleatorias
import pytest


def test_anexar_numeros_aleatorios():
    """Verifique se a função anexar_numeros_aleatorios funciona corretamente.
    Parâmetros: nenhum
    Retorno: nenhum
    """
    # Crie uma lista vazia chamada lista_numeros.
    lista_numeros = []

    # Verifique se o comprimento da lista vazia é zero.
    assert len(lista_numeros) == 0

    # Chame a função anexar_numeros_aleatorios para anexar um número.
    anexar_numeros_aleatorios(lista_numeros)

    # Verifique se a lista de números agora tem um elemento.
    assert len(lista_numeros) == 1

    # Verifique se todos os elementos da lista de números
    # são números de ponto flutuante.
    for x in lista_numeros:
        assert isinstance(x, float)

    # Chame a função anexar_numeros_aleatorios para anexar três números.
    anexar_numeros_aleatorios(lista_numeros, 3)

    # Verifique se a lista de números agora tem quatro elementos.
    assert len(lista_numeros) == 4

    # Verifique se todos os elementos da lista de números
    # são números de ponto flutuante.
    for x in lista_numeros:
        assert isinstance(x, float)


#def test_anexar_palavras_aleatorias():
#    """Verifique se a função anexar_palavras_aleatorias funciona corretamente.
#    Parâmetros: nenhum
#    Retorno: nenhum
#    """
#    lista_palavras = []
#    assert len(lista_palavras) == 0
#
#    anexar_palavras_aleatorias(lista_palavras)
#    assert len(lista_palavras) == 1
#    for palavra in lista_palavras:
#        assert isinstance(palavra, str)
#        assert len(palavra) >= 1
#
#    anexar_palavras_aleatorias(lista_palavras, 3)
#    assert len(lista_palavras) == 4
#    for palavra in lista_palavras:
#        assert isinstance(palavra, str)
#        assert len(palavra) >= 1


# Chame a função main que faz parte do pytest para que o
# computador execute as funções de teste neste arquivo.
pytest.main(["-v", "--tb=line", "-rN", __file__])
