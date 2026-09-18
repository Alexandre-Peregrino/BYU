from pytest import approx
import pytest
from fluxo_de_agua import calc_altura_coluna_agua, calc_pressao_pela_altura, calc_num_reynolds, calc_perda_pressao_conexoes, calc_perda_pressao_reducao_tubo, calc_perda_pressao_tubo, converter_kPa_para_MCA

# Melhoria:
# 1. Criação do test_converter_kPa_para_MCA para a função converter_kPa_para_MCA
# 2. Uso do decorator @pytest.mark.parametrize para agilizar o processo para múltiplos testes

@pytest.mark.parametrize(
        "altura_torre, altura_tanque, coluna_agua",
        [
            (0.0, 0.0, 0.0),
            (0.0, 10.0, 7.5),
            (25.0, 0.0, 25.0),
            (48.3, 12.8, 57.9),
        ],
)
def test_calc_altura_coluna_agua(altura_torre, altura_tanque, coluna_agua):
    esperada = calc_altura_coluna_agua(altura_torre, altura_tanque)

    assert esperada == coluna_agua

@pytest.mark.parametrize(
    "altura, pressao_esperada, aproximacao",
    [(0.0, 0.000, 0.001), 
    (30.2, 295.628, 0.001), 
    (50.0, 489.450, 0.001)],
)
def test_calc_pressao_pela_altura(altura, pressao_esperada, aproximacao):
   
    resultado_obtido = calc_pressao_pela_altura(altura)

    assert resultado_obtido == pytest.approx(
        pressao_esperada, abs=aproximacao
    )


@pytest.mark.parametrize(
        "diametro_tubo, comprimento_tubo, fator_atrito, velocidade_fluido, perda_esperada, tolerancia_approx",
        [
            (0.048692, 0.00, 0.018,	1.75, 0.000, 0.001),
            (0.048692, 200.00, 0.000, 1.75,	0.000, 0.001),
            (0.048692, 200.00, 0.018, 0.00,	0.000, 0.001),
            (0.048692, 200.00, 0.018, 1.75, -113.008, 0.001),
            (0.048692, 200.00, 0.018, 1.65, -100.462, 0.001),
            (0.286870, 1000.00, 0.013, 1.65, -61.576, 0.001),
            (0.286870, 1800.75, 0.013, 1.65, -110.884, 0.001),

        ],
)
def test_cal_perda_pressao_tubo(diametro_tubo, comprimento_tubo, fator_atrito, velocidade_fluido, perda_esperada, tolerancia_approx):
    resultado = calc_perda_pressao_tubo(diametro_tubo, comprimento_tubo, fator_atrito, velocidade_fluido)

    assert resultado == pytest.approx(perda_esperada, abs=tolerancia_approx)



@pytest.mark.parametrize(
    "velocidade_fluido, quantidade_conexoes, perda_esperada_pressao, tolerancia_approx",
    [
        (0.00, 3, 0.000, 0.001),
        (1.65, 0, 0.000, 0.001),
        (1.65, 2, -0.109, 0.001),
        (1.75, 2, -0.122, 0.001),
        (1.75, 5, -0.306, 0.001),
    ],
)
def test_calc_perda_pressao_conexoes(velocidade_fluido, quantidade_conexoes, perda_esperada_pressao, tolerancia_approx):
    resultado = calc_perda_pressao_conexoes(velocidade_fluido, quantidade_conexoes)

    assert resultado == pytest.approx(perda_esperada_pressao, abs=tolerancia_approx)



@pytest.mark.parametrize(
    "diametro_hidraulico, velocidade_do_fluido, numero_de_reynolds, tolerancia_absoluta_aproximada",
    [
        (0.048692, 0.00, 0, 1),
        (0.048692, 1.65, 80069, 1),
        (0.048692, 1.75, 84922, 1),
        (0.286870, 1.65, 471729, 1),
        (0.286870, 1.75, 500318, 1),
    ],
)
def test_calc_num_reynolds(diametro_hidraulico, velocidade_do_fluido, numero_de_reynolds, tolerancia_absoluta_aproximada):
    resultado = calc_num_reynolds(diametro_hidraulico, velocidade_do_fluido)

    assert resultado == pytest.approx(numero_de_reynolds, abs=tolerancia_absoluta_aproximada)


@pytest.mark.parametrize(
    "diametro_maior, velocidade_do_fluido, numero_de_reynolds,  diametro_menor, perda_esperada_de_pressao,  tolerancia_absoluta_approx",
    [
        (0.28687, 0.00, 1, 0.048692, 0.000, 0.001),
        (0.28687, 1.65, 471729, 0.048692, -163.744, 0.001),
        (0.28687, 1.75, 500318, 0.048692, -184.182, 0.001),
    ],
)
def test_calc_perda_pressao_reducao_tubo(diametro_maior, velocidade_do_fluido, numero_de_reynolds,  diametro_menor, perda_esperada_de_pressao,  tolerancia_absoluta_approx):
    resultado = calc_perda_pressao_reducao_tubo(diametro_maior, velocidade_do_fluido, numero_de_reynolds, diametro_menor)

    assert resultado == pytest.approx(perda_esperada_de_pressao, abs=tolerancia_absoluta_approx)


@pytest.mark.parametrize(
    "kPa, mca_esperado",
    [
        (10, 1.02),
        (20, 2.04),
        (30, 3.06),
    ],
)
def test_converter_kPa_para_MCA(kPa, mca_esperado):
    resultado = converter_kPa_para_MCA(kPa)

    assert resultado == pytest.approx(mca_esperado, abs=0.01)

  
# Chama a função main que faz parte do pytest para que o
# o computador execute as funções de teste neste arquivo.
pytest.main(["-v", "--tb=line", "-rN", __file__])
    