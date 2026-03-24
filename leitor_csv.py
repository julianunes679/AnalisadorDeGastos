import csv

def carregar_transacoes(caminho):
    transacoes = []

    with open(caminho, newline='', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            try:
                valor_convertido = float(linha["valor"])
                linha["valor"] = valor_convertido

                categoria = linha["categoria"].strip()
                if not categoria:
                    raise ValueError(f"Categoria vazia na linha: {linha}")

                linha["categoria"] = categoria

                transacoes.append(linha)

            except ValueError:
                raise ValueError(f"Erro ao processar linha: {linha}")

    return transacoes