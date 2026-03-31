import csv

def carregar_transacoes(caminho):
    transacoes = []

    with open(caminho, newline='', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            try:
                # valida valor
                valor = float(linha["valor"])
                if valor < 0:
                    raise ValueError

                # valida categoria
                categoria = linha["categoria"].strip()
                if not categoria:
                    raise ValueError

                transacoes.append({
                    "data": linha["data"],
                    "descricao": linha["descricao"],
                    "valor": valor,
                    "categoria": categoria
                })

            except Exception:
                raise ValueError(f"Erro ao processar linha: {linha}")

    return transacoes