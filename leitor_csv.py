import csv

def carregar_transacoes(caminho):
    transacoes = []

    with open(caminho, newline='', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            try:
                valor_convertido = float(linha["valor"])
                linha["valor"] = valor_convertido
                transacoes.append(linha)
            except ValueError:
                raise ValueError(f"Erro ao converter valor na linha: {linha}")

    return transacoes
