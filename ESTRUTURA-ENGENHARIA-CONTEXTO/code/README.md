# Código-Fonte

Este diretório contém o código-fonte do seu projeto.

## Estrutura Recomendada

```
/code
  ├── main.py           # Ponto de entrada principal
  ├── utils.py          # Funções utilitárias
  ├── /tests            # Testes unitários e de integração
  ├── /models           # Modelos de dados
  └── /services         # Serviços e lógica de negócio
```

## Padrões de Código

Siga os padrões definidos em `/guides/implementation.md` gerado pelo SDLC Guide.

## Engenharia de Contexto - Copilot

Para este diretório, use parâmetros de **Interpretação Literal**:
- Top-k: 1-10 (maior precisão)
- Top-p: 0.1-0.3 (sampling restrito)
- Temperature: 0.1-0.3 (baixa aleatoriedade)

Foco em: Precisão, testes, docstrings ricas, padrões de código.
