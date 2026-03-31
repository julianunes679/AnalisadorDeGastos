# 📊 Analisador de Gastos

Aplicação em Python para análise de gastos pessoais a partir de arquivos CSV, com geração de métricas e visualizações.

---

## Objetivo

Este projeto foi desenvolvido com foco em:

- Prática de manipulação de dados
- Estruturação de projetos em Python
- Aplicação de conceitos de análise de dados
- Criação de um artefato real para portfólio

---

## Funcionalidades

- Leitura de dados via CSV
- Validação e tratamento de erros
- Cálculo de métricas:
  - Total de gastos
  - Quantidade de transações
  - Média por transação
- Agrupamento de gastos por mês
- Agrupamento por categoria
- Geração de gráficos:
  - Linha (gastos mensais)
  - Pizza (distribuição por categoria)

---

## Estrutura do Projeto

AnalisadorDeGastos/
│
├── main.py
├── leitor_csv.py
├── relatorio.py
├── grafico.py
├── requirements.txt
├── README.md
│
└── dados/
└── extrato.csv


##   Saídas Geradas
Resumo financeiro no terminal
Arquivos de imagem:
grafico_mensal.png
grafico_categoria.png


##   Conceitos Aplicados
Manipulação de arquivos CSV
Estruturas de dados (listas e dicionários)
Tratamento de exceções (try/except)
Organização modular de código
Agregação de dados
Visualização com Matplotlib
