"""
repetir_textos.py

Recebe uma string e um inteiro e retorna a string repetida N vezes.
Inclui função reutilizável e execução via CLI.
"""

def repetir(texto: str, vezes: int) -> str:
    """
    Repete uma string N vezes.

    Parâmetros:
    - texto: Texto a ser repetido.
    - vezes: Número de repetições (deve ser >= 0).

    Retorna:
    - String com o texto repetido.

    Levanta:
    - ValueError: se 'vezes' for negativo.
    """
    if vezes < 0:
        raise ValueError("O número de repetições deve ser >= 0.")
    return texto * vezes


def main() -> None:
    print("=== Repetindo Textos ===")
    texto = input("Digite o texto: ")
    while True:
        try:
            vezes = int(input("Digite o número de repetições (inteiro >= 0): "))
            if vezes < 0:
                print("Valor inválido. Deve ser >= 0.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")
    resultado = repetir(texto, vezes)
    print(f"Resultado: {resultado}")


if __name__ == "__main__":
    main()
