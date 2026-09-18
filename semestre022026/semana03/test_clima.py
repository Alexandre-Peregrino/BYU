
from clima import fahr_para_celsius
from pytest import approx
import pytest
def test_fahr_para_celsius():

    assert fahr_para_celsius(-25) == approx(-31.66667)
    assert fahr_para_celsius(0) == approx(-17.77778)
    assert fahr_para_celsius(32) == approx(0)
    assert fahr_para_celsius(70) == approx(21.1111)

# Chama a função main que faz parte do pytest para que o
# o computador execute as funções de teste neste arquivo.
pytest.main(["-v", "--tb=line", "-rN", __file__])