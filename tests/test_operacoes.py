import pytest
from src.operacoes_matematicas import operar

def test_soma():
    assert operar(2, 3, "+") == 5

def test_subtracao():
    assert operar(5, 2, "-") == 3

def test_multiplicacao():
    assert operar(4, 2, "*") == 8

def test_divisao():
    assert operar(9, 3, "/") == 3

def test_divisao_por_zero():
    with pytest.raises(ZeroDivisionError):
        operar(1, 0, "/")

def test_operacao_invalida():
    with pytest.raises(ValueError):
        operar(1, 1, "%")  # operação não suportada
