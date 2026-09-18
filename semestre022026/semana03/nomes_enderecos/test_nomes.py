from nomes import criar_nome_completo, extrair_sobrenome, extrair_primeiro_nome

import pytest


def test_nome_completo():
    primeiro_nome = "Elaine"
    sobrenome = "Oliveira"
    resultado = "Oliveira; Elaine"


    saida = criar_nome_completo(primeiro_nome, sobrenome)
    assert saida == resultado


def test_extrair_sobrenome():
    nome_completo = "Peregrino; Alexandre"
    resultado = "Peregrino"

    saida = extrair_sobrenome(nome_completo)
    assert saida  == resultado


def test_extrair_primeiro_nome():
    nome_completo = "Peregrino; Alexandre"
    resultado = "Alexandre"

    saida = extrair_primeiro_nome(nome_completo)
    assert saida== resultado


pytest.main(["-v", "--tb=line", "-rN", __file__])


