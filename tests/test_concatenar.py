#### tests/test_concatenar.py
```python
import pytest
from src.concatenar_dados import concatenar

def test_concatenar_com_espaco_default():
    assert concatenar("Olá", "Mundo") == "Olá Mundo"

def test_concatenar_com_separador_customizado():
    assert concatenar("a", "b", "-") == "a-b"

def test_concatenar_convertendo_tipos():
    assert concatenar(10, 3.14, ", ") == "10, 3.14"
