import pytest
from src.repetir_textos import repetir

def test_repetir_texto_basico():
    assert repetir("ab", 3) == "ababab"

def test_repetir_zero_vezes():
    assert repetir("x", 0) == ""

def test_repetir_vezes_negativo_erro():
    with pytest.raises(ValueError):
        repetir("x", -1)
