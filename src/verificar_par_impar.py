"""
verificar_par_impar.py

Recebe um número inteiro e verifica se é par ou ímpar.
Inclui função reutilizável e execução via CLI.
"""

def eh_par(n: int) -> bool:
    """
    Retorna True se n for par, False caso contrário.
    """
    return n % 2 == 0


def main() -> None:
    print("=== Verificando Números Pares e Ímpares ===")
    while True:
        try:
            n = int(input("Digite um número inteiro: ").strip())
            break
        except ValueError:
            print("Entrada inválida. Digite um inteiro.")
    if eh_par(n):
        print(f"{n} é par.")
    else:
        print(f"{n} é ímpar.")


if __name__ == "__main__":
    main()
