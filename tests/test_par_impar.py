from src.verificar_par_impar import eh_par

def test_par():
    assert eh_par(10) is True

def test_impar():
    assert eh_par(7) is False

def test_zero_eh_par():
    assert eh_par(0) is True
