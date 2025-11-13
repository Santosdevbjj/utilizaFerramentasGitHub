"""
calcular_media.py

Calcula a média de três notas fornecidas pelo usuário.
Inclui função reutilizável e execução via CLI.
"""

from typing import Sequence


def media(notas: Sequence[float]) -> float:
    """
    Calcula a média aritmética de uma sequência de números.

    Parâmetros:
    - notas: Sequência de floats (não vazia).

    Retorna:
    - Média como float.

    Levanta:
    - ValueError: se a sequência estiver vazia.
    """
    if not notas:
        raise ValueError("A lista de notas não pode ser vazia.")
    return sum(notas) / len(notas)


def _ler_nota(indice: int) -> float:
    while True:
        try:
            valor = float(input(f"Digite a nota {indice} (0 a 10): ").strip())
            if 0 <= valor <= 10:
                return valor
            print("Nota fora do intervalo (0 a 10).")
        except ValueError:
            print("Entrada inválida. Digite um número.")


def main() -> None:
    print("=== Calculando Média de Notas ===")
    n1 = _ler_nota(1)
    n2 = _ler_nota(2)
    n3 = _ler_nota(3)
    m = media([n1, n2, n3])
    print(f"Média: {m:.2f}")


if __name__ == "__main__":
    main()
