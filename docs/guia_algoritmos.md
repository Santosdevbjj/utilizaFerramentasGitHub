# Guia dos algoritmos e boas práticas

Este guia descreve os algoritmos implementados, suas entradas/saídas e como o GitHub Copilot pode ajudar no desenvolvimento e documentação.

---

## Concatenando dados (`src/concatenar_dados.py`)
- Objetivo: Receber dois dados e concatenar em uma única string.
- Função principal: `concatenar(a, b, separador=" ") -> str`
- Dicas:
  - Use o Copilot para sugerir variações de formatação (f-strings, `join`).
  - Valide entradas e ofereça separador opcional.

## Repetindo textos (`src/repetir_textos.py`)
- Objetivo: Repetir uma string N vezes.
- Função principal: `repetir(texto: str, vezes: int) -> str`
- Dicas:
  - Trate `vezes < 0` com `ValueError`.
  - Sugestões do Copilot podem incluir manipulação de espaço/linha.

## Operações matemáticas simples (`src/operacoes_matematicas.py`)
- Objetivo: Operar entre dois números: `+`, `-`, `*`, `/`.
- Função principal: `operar(a: float, b: float, op: Literal["+", "-", "*", "/"]) -> float`
- Dicas:
  - Trate divisão por zero (`ZeroDivisionError`).
  - O Copilot ajuda a criar menus CLI e validações.

## Verificando números pares e ímpares (`src/verificar_par_impar.py`)
- Objetivo: Indicar se um número inteiro é par ou ímpar.
- Função principal: `eh_par(n: int) -> bool`
- Dicas:
  - Introduza testes simples e condicionais.
  - Copilot sugere mensagens amigáveis para CLI.

## Calculando média de notas (`src/calcular_media.py`)
- Objetivo: Calcular a média de três notas (0 a 10).
- Função principal: `media(notas: Sequence[float]) -> float`
- Dicas:
  - Valide que a lista não esteja vazia.
  - Copilot pode sugerir arredondamento e formatação.

## Verificando palíndromos (`src/verificar_palindromo.py`)
- Objetivo: Verificar se texto é palíndromo após normalização.
- Funções:
  - `normalizar(texto: str) -> str`
  - `eh_palindromo(texto: str) -> bool`
- Dicas:
  - Use regex para limpar o texto.
  - Copilot sugere utilitários para normalização e testes.

---

## Como executar localmente

1. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
