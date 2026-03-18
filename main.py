from leitor_csv import carregar_transacoes
from relatorio import gerar_resumo, gastos_por_mes
from grafico import gerar_grafico

def main():
    try:
        transacoes = carregar_transacoes("dados/extrato.csv")
        resumo = gerar_resumo(transacoes)
        gastos_mensais = gastos_por_mes(transacoes)

        print("Resumo Financeiro")
        print("-----------------")
        print(f"Total gasto: R$ {resumo['total']:.2f}")
        print(f"Quantidade de transações: {resumo['quantidade']}")
        print(f"Média por transação: R$ {resumo['media']:.2f}")

        print("\nGastos por mês")
        print("--------------")

        for mes in sorted(gastos_mensais):
            valor = gastos_mensais[mes]
            print(f"{mes} → R$ {valor:.2f}")

        # ✅ AQUI é o lugar correto
        gerar_grafico(gastos_mensais)

    except ValueError as erro:
        print("Erro ao processar o arquivo.")
        print(erro)

if __name__ == "__main__":
    main()