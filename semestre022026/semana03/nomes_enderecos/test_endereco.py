from endereco import extrair_cidade
import pytest


def test_extrair_cidade():
    endereco = "legal, 07, canaã, celestial - céu,59000000"
    cidade = "legal"

    saida = extrair_cidade(endereco)
    assert saida == cidade

pytest.main(["-v", "--tb=line", "-rN", __file__])
