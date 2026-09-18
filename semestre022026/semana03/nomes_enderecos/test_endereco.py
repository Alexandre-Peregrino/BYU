from endereco import extrair_cidade, extrair_estado, extrair_cep
import pytest


def test_extrair_cidade():
    endereco = "legal, 07, canaã, celestial - céu,59000000"
    cidade = "celestial"

    saida = extrair_cidade(endereco)
    assert saida == cidade


def test_extrair_estado():
    endereco = "legal, 07, canaã, celestial - céu,59000000"
    estado = "céu"

    saida = extrair_estado(endereco)
    assert saida == estado


def test_extrair_cep():
    endereco = "legal, 07, canaã, celestial - céu,59000000"
    cep = "59000000"

    saida = extrair_cep(endereco)
    assert saida == cep



pytest.main(["-v", "--tb=line", "-rN", __file__])
