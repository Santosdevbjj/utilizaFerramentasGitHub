"""
operacoes_matematicas.py

Solicita dois números e uma operação simples e retorna o resultado.
Inclui função reutilizável e execução via CLI.
"""

from typing import Literal

Operacao = Literal["+", "-", "*", "/"]


def operar(a: float, b: float, op: Operacao) -> float:
    """
    Executa operação matemática simples entre dois números.

    Parâmetros:
    - a: Primeiro número.
    - b: Segundo número.
    - op: Operação ('+', '-', '*', '/').

    Retorna:
    - Resultado da operação como float.

    Levanta:
    - ValueError: operação inválida.
    - ZeroDivisionError: divisão por zero.
    """
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        if b == 0:
            raise ZeroDivisionError("Divisão por zero não permitida.")
        return a / b
    raise ValueError(f"Operação inválida: {op}")


def _ler_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Entrada inválida. Digite um número (ex.: 10, 3.14).")


def main() -> None:
    print("=== Operações Matemáticas Simples ===")
    a = _ler_float("Digite o primeiro número: ")
    b = _ler_float("Digite o segundo número: ")
    op = input("Escolha a operação (+, -, *, /): ").strip()
    try:
        resultado = operar(a, b, op)  # type: ignore[arg-type]
        print(f"Resultado: {resultado}")
    except (ValueError, ZeroDivisionError) as e:
        print(f"Erro: {e}")


if __name__ == "__main__":
    main()
