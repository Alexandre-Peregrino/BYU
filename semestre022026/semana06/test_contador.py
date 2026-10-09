from contador import normalizar_texto, contar_palavras, ordenar_contagem


def test_normalizar_texto():
    resultado = normalizar_texto("Olá, Mundo! Tudo bem?")
    assert resultado == "olá mundo tudo bem"


def test_contar_palavras():
    resultado = contar_palavras("gato gato cachorro passarinho cachorro gato")
    assert resultado == {"gato": 3, "cachorro": 2, "passarinho": 1}


def test_ordenar_contagem():
    contagem = {"gato": 3, "cachorro": 2, "passarinho": 1}
    resultado = ordenar_contagem(contagem)
    assert resultado == [("gato", 3), ("cachorro", 2), ("passarinho", 1)]