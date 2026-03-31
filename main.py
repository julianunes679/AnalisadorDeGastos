from leitor_csv import carregar_transacoes
from relatorio import gerar_resumo, gastos_por_mes, gastos_por_categoria
from grafico import grafico_mensal, grafico_categoria


def main():
    try:
        transacoes = carregar_transacoes("dados/extrato.csv")

        resumo = gerar_resumo(transacoes)
        mensal = gastos_por_mes(transacoes)
        categoria = gastos_por_categoria(transacoes)

        print("Resumo Financeiro")
        print("-----------------")
        print(f"Total: R$ {resumo['total']:.2f}")
        print(f"Qtd: {resumo['quantidade']}")
        print(f"Média: R$ {resumo['media']:.2f}")

        print("\nPor mês")
        print("-------")
        for mes in sorted(mensal):
            print(f"{mes} → R$ {mensal[mes]:.2f}")

        print("\nPor categoria")
        print("-------------")
        for cat, val in categoria.items():
            print(f"{cat} → R$ {val:.2f}")

        grafico_mensal(mensal)
        grafico_categoria(categoria)

        print("\nGráficos salvos: grafico_mensal.png e grafico_categoria.png")

    except ValueError as e:
        print("Erro:", e)


if __name__ == "__main__":
    main()