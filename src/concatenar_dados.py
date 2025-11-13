"""
concatenar_dados.py

Recebe dois dados do usuário e concatena em uma única string.
Inclui função reutilizável e execução via CLI.
"""

from typing import Any


def concatenar(a: Any, b: Any, separador: str = " ") -> str:
    """
    Concatena dois valores como strings com um separador.

    Parâmetros:
    - a: Primeiro valor (qualquer tipo, será convertido para string).
    - b: Segundo valor (qualquer tipo, será convertido para string).
    - separador: String usada entre os dois valores (default: espaço).

    Retorna:
    - String concatenada.
    """
    return f"{str(a)}{separador}{str(b)}"


def _input_nao_vazio(prompt: str) -> str:
    """Solicita entrada não vazia."""
    while True:
        valor = input(prompt).strip()
        if valor:
            return valor
        print("Entrada vazia. Tente novamente.")


def main() -> None:
    print("=== Concatenando Dados ===")
    dado1 = _input_nao_vazio("Digite o primeiro dado: ")
    dado2 = _input_nao_vazio("Digite o segundo dado: ")
    sep = input("Opcional: informe um separador (Enter para espaço): ").strip() or " "
    resultado = concatenar(dado1, dado2, sep)
    print(f"Resultado: {resultado}")


if __name__ == "__main__":
    main()
