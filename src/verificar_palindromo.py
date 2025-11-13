"""
verificar_palindromo.py

Verifica se uma palavra ou frase é um palíndromo.
Inclui função reutilizável e execução via CLI.
"""

import re


def normalizar(texto: str) -> str:
    """
    Remove caracteres não alfanuméricos e coloca em minúsculas.
    """
    return re.sub(r"[^0-9a-zA-Z]+", "", texto).lower()


def eh_palindromo(texto: str) -> bool:
    """
    Retorna True se 'texto' for palíndromo após normalização.
    """
    t = normalizar(texto)
    return t == t[::-1]


def main() -> None:
    print("=== Verificando Palíndromos ===")
    texto = input("Digite uma palavra ou frase: ").strip()
    if not texto:
        print("Entrada vazia.")
        return
    if eh_palindromo(texto):
        print("É palíndromo!")
    else:
        print("Não é palíndromo.")


if __name__ == "__main__":
    main()
