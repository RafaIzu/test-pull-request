import pytest

from main import calcular_desconto, calcular_desconto_black_friday, calcular_imposto


def test_calcular_desconto():

    resultado = calcular_desconto(1000, 10)

    assert resultado == 900


def test_calcular_desconto_zero():

    resultado = calcular_desconto(500, 0)

    assert resultado == 500


def test_calcular_imposto():

    resultado = calcular_imposto(1000, 10)

    assert resultado == 100


def test_valor_negativo():

    with pytest.raises(ValueError):
        calcular_desconto(-100, 10)
        calcular_desconto_black_friday(-100, 10)


def test_percentual_invalido():

    with pytest.raises(ValueError):
        calcular_desconto(100, 150)
        calcular_desconto_black_friday(100, 150)


def test_calcular_desconto_black_friday():

    resultado = calcular_desconto_black_friday(500, 10)
    assert resultado == 425


def test_calcular_desconto_zero_black_friday():

    resultado = calcular_desconto_black_friday(500, 0)

    assert resultado == 500