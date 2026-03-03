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
