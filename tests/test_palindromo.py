from src.verificar_palindromo import eh_palindromo, normalizar

def test_normalizar_remove_nao_alfanumericos():
    assert normalizar("A man, a plan, a canal: Panama!") == "amanaplanacanalpanama"

def test_palindromo_simples():
    assert eh_palindromo("arara") is True

def test_palindromo_frase_com_espacos_e_pontuacao():
    assert eh_palindromo("Roma é amor!") is True

def test_nao_palindromo():
    assert eh_palindromo("python") is False
