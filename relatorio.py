def gerar_resumo(transacoes):
    total = sum(t["valor"] for t in transacoes)
    quantidade = len(transacoes)
    media = total / quantidade if quantidade > 0 else 0

    return {
        "total": total,
        "quantidade": quantidade,
        "media": media
    }


def gastos_por_mes(transacoes):
    resumo = {}

    for t in transacoes:
        mes = t["data"][:7]
        resumo[mes] = resumo.get(mes, 0) + t["valor"]

    return resumo


def gastos_por_categoria(transacoes):
    resumo = {}

    for t in transacoes:
        cat = t["categoria"]
        resumo[cat] = resumo.get(cat, 0) + t["valor"]

    return resumo