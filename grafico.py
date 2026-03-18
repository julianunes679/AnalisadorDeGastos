import matplotlib.pyplot as plt

def gerar_grafico(gastos_mensais):
    meses = sorted(gastos_mensais.keys())
    valores = [gastos_mensais[mes] for mes in meses]

    plt.figure()
    plt.plot(meses, valores)
    plt.title("Gastos por mês")
    plt.xlabel("Mês")
    plt.ylabel("Valor (R$)")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.show()