def gerar_resumo(transacoes):
    total = 0

    for transacao in transacoes:
        total += transacao["valor"]

    quantidade = len(transacoes)

    if quantidade > 0:
        media = total / quantidade
    else:
        media = 0

    return {
        "total": total,
        "quantidade": quantidade,
        "media": media
    }

def gastos_por_mes(transacoes):
    resumo_mensal = {}

    for transacao in transacoes: 
        data = transacao["data"]
        valor = transacao["valor"]

        mes = data[:7]

        if mes not in resumo_mensal:
            resumo_mensal[mes] = 0

            resumo_mensal[mes] += valor

        return resumo_mensal