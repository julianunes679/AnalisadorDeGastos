import matplotlib.pyplot as plt

def grafico_mensal(gastos_mensais):
    meses = sorted(gastos_mensais.keys())
    valores = [gastos_mensais[m] for m in meses]

    plt.figure()
    plt.plot(meses, valores)
    plt.title("Gastos por mês")
    plt.xlabel("Mês")
    plt.ylabel("Valor (R$)")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig("grafico_mensal.png")
    plt.close()


def grafico_categoria(gastos_categoria):
    categorias = list(gastos_categoria.keys())
    valores = list(gastos_categoria.values())

    plt.figure()
    plt.pie(valores, labels=categorias, autopct="%1.1f%%")
    plt.title("Gastos por categoria")
    plt.tight_layout()

    plt.savefig("grafico_categoria.png")
    plt.close()