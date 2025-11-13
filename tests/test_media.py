import pytest
from src.calcular_media import media

def test_media_tres_notas():
    assert media([7.0, 8.0, 9.0]) == pytest.approx(8.0)

def test_media_lista_unica():
    assert media([10.0]) == pytest.approx(10.0)

def test_media_lista_vazia_erro():
    with pytest.raises(ValueError):
        media([])
